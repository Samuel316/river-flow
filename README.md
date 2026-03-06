# River Flow
Real-time water level dashboard. Built with Python and Plotly, using the Environment Agency Flood Monitoring API. Automatically deployed via GitLab Pages. 

## Dependencies

- [uv](https://docs.astral.sh/uv/getting-started/)

## Setup


### Install in development mode

```bash
uv sync
```

## Project Structure

```
river-flow/
├── src/                  # Source code
├── tests/                # Unit tests
├── pyproject.toml        # Project metadata and build configuration
└── README.md             # This file
```

## Usage

```python
from template_project import main

main.run()
```

## Development

### Running tests

```bash
pytest
```


## License

MIT

