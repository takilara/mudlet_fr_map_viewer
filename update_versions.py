import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--update_version",action="store_true",help="Update the files")
parser.add_argument("--version")
args = parser.parse_args()


with open("versions.json","r") as fp: 
    versions = json.load(fp)

print("Current versions")
print(versions)



# add new version if relevant
if args.update_version:
    if args.version:
        print("Add version {} to txt file".format(args.version))
        if "versions" not in versions.keys():
            versions["versions"] = []
        
        if args.version not in versions["versions"]:
            versions["versions"].append(args.version)
        print(versions)
        with open("versions.json","w") as fp: 
            json.dump(versions,fp,indent=4, sort_keys=True)



# construct lua
with open("versions.json","r") as fp: 
    versions = json.load(fp)


lines = []
lines.append("return {{")
if "versions" not in versions.keys():
    versions["versions"] = []
cnt = 1
for v in versions["versions"]:
    lines.append("\t[{}] = [[{}]],".format(cnt,v))
    cnt = cnt + 1

lines[-1] = lines[-1][:-1]

lines.append("\t},")
lines.append("}")

print("\n".join(lines))

if args.update_version:
    with open("versions.lua","w") as fp:
        fp.write("\n".join(lines))


        



