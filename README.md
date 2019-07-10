# `griddy`: Generate CSS grid layouts FAST
<p align=center>
<img src="./assets/logo.png" width="200">
</p>

> Tired of manually splitting `<div>`'s? Try **`griddy`**.
## Setup 
### Build from source
```
git clone https://github.com/Mckinsey666/griddy.git
cd griddy
pip install .
```
### From **PyPI**
```
pip install griddy
```

## Usage
### Defining a `layout.json` file
A layout `.json` file should follow the following syntax:
- The json file contains one `json` object.
- Key of the first level of the `json` object should always be `root`.
- For other levels, the keys should follow the convention:
    - `percentage`: percentage of the children `<div>`'s height or width with respect to its parent.
    - `layout type`: defines a column layout or a row layout (column layouts will be inside a flex container). If `r` is specified, the percentage is the relative height; if `c` is specified, the percentage is the relative width.
    - `id` (optional): a unique id (can just be integers) to prevent duplicate keys in a `json` object.

```
key = percentage + layout type + id
```

- For keys in the same level, their layout types should be the same.
- For keys in the same level, it is better that their percentage add up to 100.
- If no more `<div>`s are to be splitted, set the value of the key to be `null`.

#### Sample `layout.json` file
```json
{
    "root":{
        "70r":{
            "10c": null,
            "20c": {
                "10r": null,
                "90r": null
            },
            "70c": {
                "50r1": null,
                "50r2": {
                    "20c1": null,
                    "20c2": null,
                    "60c": null
                }
            }
        },
        "30r": {
            "80c": null,
            "20c": null
        }
    }
}
```
Play with more examples in the `examples` directory.

#### Sample `index.html` output

<p align=center>
<img src="./assets/sample.png" width="600">
</p>

Each `<div>` is randomly colored for the sake of clarity. If you are a boring person, you can specify a `--no-color` argument. 

### Generate `html` and `css`
```
griddy <name of the layout file>
```
An `index.html` file and a `styles.css` file will be generated in the same directory where layout json file resides. You can simply plugin the generated grid `<div>` (top-level `<div>` of class `root` with style `width: 100%; height:100%`) anywhere in your existing code.

### Command-line arguments
|Arguments|Type|default|Explanation|
|---|---|---|---|
|**--no-color**|bool|True|Whether to color the `<div>`s|
