import os
import struct
import UnityPy

EXPORTABLE = ["Sprite", "Texture2D", "TextAsset"]


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(path, "asset_index"), "rb")
    index = read_asset_index(f)

    blocks = os.path.join(path, "blocks_export")
    ext = os.path.join(path, "export")

    for root, dirs, files in os.walk(blocks):
        for fp in files:
            env = UnityPy.load(os.path.join(root, fp))
            for ref, obj in env.container.items():
                if "/" in ref:
                    fp = os.path.join(ext, *ref.split("/"))
                else:
                    try:
                        fp = os.path.join(ext, *index[int(ref)].split("/"))
                    except KeyError:
                        print(ref)
                        continue

                if not export_object(obj, fp, False):
                    for obj in env.objects:
                        export_object(obj, fp, True)


def export_object(obj, fp, add_name=False):
    if obj.type not in EXPORTABLE:
        return False

    data = obj.read()

    if add_name:
        fp = os.path.join(fp, data.name)

    os.makedirs(os.path.dirname(fp), exist_ok=True)

    if obj.type == "TextAsset":
        with open(fp + ".txt", "wb") as f:
            f.write(obj.read().script)
    elif obj.type in ["Sprite", "Texture2D"]:
        try:
            obj.read().image.save(fp + ".png")
        except:
            pass

    return True


def read_asset_index(f):
    # unity stuff
    ulen = read_u_int(f)
    ustuff = []
    for i in range(ulen):
        dll = read_string(f)
        typ = read_string(f)
        ustuff.append((dll, typ))

    # assetlist
    alen = read_u_int(f)
    assetlist = []
    for i in range(alen):
        num = f.read(5)
        container_ref = read_int(f)
        o = f.read(3)  # 000 ???? - not aligned...probably
        path = read_string(f)

        assetlist.append((num, container_ref, path))

    # keys ????
    
    return {a[1]: a[2] for a in assetlist}


def read_int(f):
    return struct.unpack("<i", f.read(4))[0]


def read_u_int(f):
    return struct.unpack("<I", f.read(4))[0]


def read_string(f):
    str_len = read_u_int(f)
    return f.read(str_len).decode()


if __name__ == "__main__":
    main()
