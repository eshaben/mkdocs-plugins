# Test for the Minify Plugin

This directory contains a simple and focused test suite for the Minify-Plugin.

## Run Tests

```bash
pytest tests/minify/
```

## Run Tests with Verbose Output

```bash
pytest tests/minify/ -v
```

## `test_minify.py`

A single, comprehensive test file that covers all plugin functionality with one test per main feature:

- **`test_plugin_init`** - Plugin initialization and configuration
- **`test_minify_js`** - JavaScript minification functionality
- **`test_minify_css`** - CSS minification functionality  
- **`test_minify_html`** - HTML minification functionality
- **`test_asset_naming`** - Minified file naming with/without hashes
- **`test_scoped_css_gathering`** - Scoped CSS file collection
- **`test_integration_build`** - Full MkDocs integration test
- **`test_error_handling`** - Error handling for malformed content
- **`test_none_inputs`** - Handling of None inputs

## Test Coverage

The test suite covers all essential functionality:
- ✅ Plugin initialization and configuration
- ✅ HTML minification with various options
- ✅ JS/CSS minification
- ✅ Cache-safe hashing
- ✅ Scoped CSS functionality
- ✅ Error handling and edge cases
- ✅ Full MkDocs integration
- ✅ Input validation
