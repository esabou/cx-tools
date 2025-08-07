---

````markdown
# Bulk Activate / Deactivate Snyk Projects

A toolkit to **bulk activate or deactivate** projects across multiple Snyk Organizations in a Group using the Snyk API.

---

## Features

- `get_projects.py` – Gathers project data for all organizations in a Snyk Group. Uses [Snyk's REST API](https://apidocs.snyk.io/).
- `filter_projects.py` – Interactively filters projects by type (`iac`, `container`, `code`) and status (`active`, `inactive`) before any changes are made.
- `change_proj_status.py` – Activates or deactivates selected projects using [Snyk's V1 API](https://snyk.docs.apiary.io/).

---

## Configuration

Install dependencies:

```sh
pip install -r requirements.txt
````

Update variables in `get_projects.py` if needed:

```python
API_VERSION = "2024-08-15"  # Adjust to latest API version
RATE_LIMIT_DELAY = 0.2      # Throttle requests if needed
```

---

## Usage

### 1. Gather Project Information

Use the `get_projects.py` script to extract all project metadata from your Snyk Group:

```sh
python3 get_projects.py --group YOUR_GROUP_ID --token YOUR_API_TOKEN
```

Output:
A file called `project_data.json` will be created.

Example entry:

```json
{
  "org_name": "Test_Org",
  "org_id": "**************",
  "project_name": "nodejs-goof/nodejs-goof(main)",
  "project_id": "**************",
  "project_type": "sast",
  "target_file": "",
  "status": "active"
}
```

---

### 2. Filter Projects (optional but recommended)

Use the interactive `filter_projects.py` script to select only the projects you want to act on:

```sh
python3 filter_projects.py
```

You will be prompted to select:

* What **types** of projects to keep: `container`, `iac`, `code`
* What **status** to keep: `active`, `inactive`, or `both`

Output:
A new file called `filtered_project_data.json` containing only the filtered entries.

---

### 3. Activate / Deactivate Projects

Run the final step using the filtered project list:

```sh
python3 change_proj_status.py filtered_project_data.json --action activate --token YOUR_API_TOKEN
```

Replace `activate` with `deactivate` to change project status accordingly.

---

## Notes

* All scripts are meant to be run locally.
* The scripts assume you have admin access to the Snyk Group and its orgs.
* Make sure your API token has the required permissions.

---

## License

MIT

```
