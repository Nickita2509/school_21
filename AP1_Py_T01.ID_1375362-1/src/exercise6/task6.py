import json
import os

if not os.path.exists("input.txt"):
    print("File not found")
elif os.path.getsize("input.txt") == 0:
    print("Empty file")
else:
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            data = json.load(f)
        list1 = data["list1"]
        list2 = data["list2"]

        merged_list= list1 + list2
        merged_list.sort(key=lambda movie: movie["year"])
        list0 = {"list0": merged_list}

        print(json.dumps(list0, indent=4, ensure_ascii=False))

    except json.JSONDecodeError:
        print("Invalid JSON!")
    except TypeError:
        print("Invalid JSON!")