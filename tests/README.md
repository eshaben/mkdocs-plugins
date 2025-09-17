# Test Suite for mkdocs-minify-plugin

This directory contains a simple and focused test suite for the mkdocs-minify-plugin.

## Test File

### `test_simple.py`
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

## Running Tests

### Run all tests
```bash
pytest
```

### Run the simple test file
```bash
pytest tests/test_simple.py
```

### Run tests with verbose output
```bash
pytest -v
```

### Run tests with coverage
```bash
pytest --cov=mkdocs_minify_plugin
```

## Test Configuration

The test suite uses pytest with configuration in `pytest.ini`:
- Test discovery: `test_*.py` files in the `tests` directory
- Verbose output and colored output enabled
- Strict markers and disabled warnings

## Test Philosophy

This simplified test suite follows the principle of **one test per function**:
- Each test focuses on a single, specific functionality
- Tests are self-contained and don't depend on complex fixtures
- Integration tests use temporary directories created on-the-fly
- Error handling tests verify graceful degradation

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

## Dependencies

The test suite requires:
- pytest
- mkdocs
- htmlmin
- jsmin
- csscompressor
- packaging

These are listed in `requirements.txt` and `tests/requirements.txt`.