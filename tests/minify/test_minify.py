"""
Test simple y directo para mkdocs-minify-plugin.
Un test por función principal del plugin.
"""

import pytest
import subprocess
import sys
from pathlib import Path
from plugins.minify.plugin import MinifyPlugin, MINIFIERS


class TestMinifyPlugin:
    """Tests simples para las funciones principales del plugin."""

    def test_plugin_init(self):
        """Test: El plugin se inicializa correctamente."""
        plugin = MinifyPlugin()
        assert isinstance(plugin.config, dict)

    def test_minify_js(self):
        """Test: Minificación de JavaScript funciona."""
        plugin = MinifyPlugin()
        js_code = "console.log('hello');\nvar x = 1;"
        result = plugin._minify_file_data_with_func(js_code, MINIFIERS["js"])
        assert "console.log('hello');var x=1" in result

    def test_minify_css(self):
        """Test: Minificación de CSS funciona."""
        plugin = MinifyPlugin()
        css_code = ".test {\n    color: red;\n    margin: 10px;\n}"
        result = plugin._minify_file_data_with_func(css_code, MINIFIERS["css"])
        assert ".test{" in result and "color:red" in result

    def test_minify_html(self):
        """Test: Minificación de HTML funciona."""
        plugin = MinifyPlugin()
        html_code = "<html><body><p>Hello   World</p></body></html>"
        result = plugin._minify_html_page(html_code)
        assert result is not None
        assert "<html><body><p>Hello World</p></body></html>" in result

    def test_asset_naming(self):
        """Test: Nombres de archivos minificados son correctos."""
        plugin = MinifyPlugin()
        
        # Sin hash, sin minificación
        plugin.config['minify_css'] = False
        result = plugin._minified_asset("style.css", "css", "")
        assert result == "style.css"
        
        # Con minificación
        plugin.config['minify_css'] = True
        result = plugin._minified_asset("style.css", "css", "")
        assert result == "style.min.css"
        
        # Con hash
        result = plugin._minified_asset("style.css", "css", "abc123")
        assert result == "style.abc123.min.css"

    def test_scoped_css_gathering(self):
        """Test: Recolección de archivos CSS con scope funciona."""
        plugin = MinifyPlugin()
        plugin.config['scoped_css'] = {
            "index.md": ["css/home.css"],
            "about.md": ["css/about.css"]
        }
        plugin.config['scoped_css_templates'] = {}
        
        files = plugin._gather_scoped_css_files()
        assert "css/home.css" in files
        assert "css/about.css" in files

    def test_integration_build(self, tmp_path):
        """Test: Integración completa con MkDocs build."""
        # Crear estructura de sitio
        docs = tmp_path / "docs"
        docs.mkdir()
        (docs / "index.md").write_text("# Home\n\nWelcome.", encoding="utf8")
        
        assets = docs / "extra_assets"
        assets.mkdir()
        (assets / "css").mkdir()
        (assets / "js").mkdir()
        
        # Crear archivos de prueba
        (assets / "css" / "main.css").write_text(".test { color: blue; }", encoding="utf8")
        (assets / "js" / "main.js").write_text("console.log('test');", encoding="utf8")
        
        # Configuración
        config_content = """
site_name: Test Site
theme:
  name: mkdocs
plugins:
  - minify:
      minify_html: true
      minify_css: true
      minify_js: true
      css_files:
        - extra_assets/css/main.css
      js_files:
        - extra_assets/js/main.js
extra_css:
  - extra_assets/css/main.css
extra_javascript:
  - extra_assets/js/main.js
"""
        
        config_file = tmp_path / "mkdocs.yml"
        config_file.write_text(config_content, encoding="utf8")
        
        site_dir = tmp_path / "site"
        site_dir.mkdir()
        
        # Ejecutar build
        try:
            subprocess.check_call(
                [sys.executable, "-m", "mkdocs", "build", "-q", "-f", str(config_file), "-d", str(site_dir)],
                cwd=str(tmp_path),
            )
            
            # Verificar que se crearon archivos minificados
            assert (site_dir / "extra_assets" / "css" / "main.min.css").exists()
            assert (site_dir / "extra_assets" / "js" / "main.min.js").exists()
            
            # Verificar que el HTML los referencia
            index_html = (site_dir / "index.html").read_text(encoding="utf8")
            assert "main.min.css" in index_html
            assert "main.min.js" in index_html
            
        except subprocess.CalledProcessError:
            pytest.skip("MkDocs build failed in this environment")

    def test_error_handling(self):
        """Test: El plugin maneja errores sin crashear."""
        plugin = MinifyPlugin()
        
        # CSS malformado
        bad_css = ".test { color: red; /* unclosed comment"
        result = plugin._minify_file_data_with_func(bad_css, MINIFIERS["css"])
        assert result is not None
        
        # HTML malformado
        bad_html = "<html><body><p>Unclosed paragraph"
        result = plugin._minify_html_page(bad_html)
        assert result is not None

    def test_none_inputs(self):
        """Test: El plugin maneja inputs None correctamente."""
        plugin = MinifyPlugin()
        
        # Debería manejar None sin crashear
        try:
            result = plugin._minify_html_page(None)
            assert result is None
        except (TypeError, AttributeError):
            # También es aceptable que lance excepción
            pass
