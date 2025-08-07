import json

# Define the project type categories
containerTypes = ["deb", "linux", "dockerfile", "rpm", "apk"]
iacTypes = ["k8sconfig", "helmconfig", "terraformconfig", "armconfig", "cloudformationconfig"]
codeTypes = ["sast"]

category_map = {
    "container": containerTypes,
    "iac": iacTypes,
    "code": codeTypes
}

input_file = "project_data.json"
output_file = "filtered_project_data.json"

def ask_project_types():
    print("Which types of projects would you like to keep?")
    print("Choose one or more from: container, iac, code")
    user_input = input("Enter your selection (e.g., container,code): ").lower().strip()
    selected_categories = [s.strip() for s in user_input.split(",")]

    selected_types = []
    for cat in selected_categories:
        if cat in category_map:
            selected_types.extend(category_map[cat])
        else:
            print(f"⚠️  '{cat}' is not a valid category. Ignoring.")

    if not selected_types:
        print("❌ No valid project type selected. Exiting.")
        exit(1)

    return set(selected_types)

def ask_status_filter():
    print("\nWhich project status would you like to keep?")
    print("Options: active, inactive, both")
    status_input = input("Enter status (e.g., active): ").lower().strip()

    if status_input == "both":
        return {"active", "inactive"}
    elif status_input in {"active", "inactive"}:
        return {status_input}
    else:
        print("❌ Invalid status selection. Exiting.")
        exit(1)

def filter_projects(allowed_types, allowed_status):
    with open(input_file, "r") as f:
        all_projects = json.load(f)

    filtered_projects = [
        project for project in all_projects
        if project.get("project_type") in allowed_types and project.get("status") in allowed_status
    ]

    with open(output_file, "w") as f:
        json.dump(filtered_projects, f, indent=4)

    print(f"\n✅ Filtered {len(filtered_projects)} out of {len(all_projects)} projects.")
    print(f"💾 Saved filtered results to: {output_file}")

if __name__ == "__main__":
    print("📁 Filtering projects from:", input_file)
    types_to_keep = ask_project_types()
    status_to_keep = ask_status_filter()
    filter_projects(types_to_keep, status_to_keep)

