with open("inputDescription.m", "r") as id:
    with open("temp.txt", "w") as temp:
        temp.write(
            "============================== ============================== =============== ============================== =============================================\n"
        )
        temp.write(
            "                   name               type                         size             default                     example \n"
        )
        temp.write(
            "============================== ============================== =============== ============================== =============================================\n"
        )

        for line in id.readlines():
            if line.startswith("desc"):
                print("line:\n", line)
                item = line.replace("desc.", "").split("=")[0]
                print("item:\n", item)
                data = line.replace("desc.", "").split("=")[1].strip("\n")
                nameList = item.split(".")[:-1]
                str = "."
                print(nameList)
                name = str.join(nameList)

                if nameList[0] == "mi":
                    break

                column = item.split(".")[-1]
                if column == "type ":
                    typedata = data.replace("'", "")
                elif column == "size ":
                    sizedata = data
                elif column == "default ":
                    defaultdata = data
                # elif column == 'description ':
                #     descriptiondata = '`%s`' % data
                elif column == "example ":
                    exampledata = line.strip("desc.").split("example = ")[1].strip("\n")
                # elif column == 'component ':
                #     componentdata = data
                # elif column == 'level ':
                #     leveldata = data
                else:
                    # print(name)
                    pass
            else:  # blank line
                temp.write(
                    "{:30} {:30} {:15} {:30} {:15}\n".format(
                        name, typedata, sizedata, defaultdata, exampledata
                    )
                )
                # temp.write('{:30} {:15} {:15} {:15} {:15} {:15} {:15} {:15}\n'.format(name, typedata, sizedata,
                #                                                                       defaultdata, descriptiondata, exampledata, componentdata, leveldata))
                typedata = ""
                sizedata = ""
                defaultdata = ""
                descriptiondata = ""
                exampledata = ""
                componentdata = ""
                leveldata = ""

        temp.write(
            "============================== ============================== =============== ============================== =============================================\n"
        )
print("done")
