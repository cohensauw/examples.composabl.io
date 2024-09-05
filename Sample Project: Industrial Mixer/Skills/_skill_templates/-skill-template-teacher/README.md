# README

This is a template for creating a new skill. A skill is a component that is responsible for making decisions to perform all or part of a task.

## Tree Structure

The template is structured as follows:

```bash
my-skill/           # Root folder
├── my_skill/       # Main package folder
│   ├── __init__.py     # Package init file
│   └── skill.py        # Main skill file
├── pyproject.toml      # Project configuration, containing [composabl]
```

## PyProject [composabl] Section

We add the `[composabl]` section to the `pyproject.toml` file to specify the type of component we are creating as well as its entrypoint. This is used by the Composabl CLI to determine the type of
component and how to handle it.

Example:

```
[composabl]
type = "teacher"
entrypoint = "my_skill.skill:MySkill"
```

## Development

To work on the skill, you can simply create a temporary file or main file that starts up and executes the `compute` method of the portable skill. Example, we can create a `test.py` file with:

```python
from composabl_skill_my_skill.skill import MySkill


async def start():
    p = MySkill()
    res = await t.compute(None, [1.0])
    print(res)


if __name__ == "__main__":
    import asyncio

    asyncio.run(start())
```

Which we can then run with

```bash
# Install the module
pip install -e my-skill

# Run the test file
python my-skill/test.py
```

### Preparing for Upload

Once we are ready for uploading, we can create a `.tar.gz` file that contains the version. This can be done with the following command:

```bash
# Tar GZ the plugin
tar -czvf my-skill-0.0.1.tar.gz my-skill
```
