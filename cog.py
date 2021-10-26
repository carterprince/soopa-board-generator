import re

output = ""

with open('output') as o: output = o.read()

output = '\n'.join(output.split("\n")[35:])

output = output.split("\n\n\n")

newOutput = []

for cog in output:
    cogData = cog.split("\n")
    for i, j in enumerate(cogData):
        cogData[i] = re.sub(": +", ":", j)

    newOutput.append(cogData)

for i in range(len(newOutput)):
    del newOutput[i][0]

#for x in newOutput:
#    if not x[0].startswith("Type"):
#        print(x)

def add_html(string):
    with open("output.html", 'a') as h:
        h.write(string+"\n")


def set_html(string):
    with open("output.html", 'w') as h:
        h.write(string)

set_html("""<html>
    <head>
    </head>
    <body style="background-color:rgb(20,20,20)">
    """)

#

finalData = []

for cog in newOutput:
    if not cog[0].startswith("Type"):
        finalData.append(cog)


#for y in range(8):
#    for x in range(12):

add_html("<div style=\"position:absolute;top:5;left:5;border-style:solid;height:400;width:600\">")

for cog in finalData:
    print(cog)


    cogType = cog[1].lower().replace("type:","")+".png"

    if cogType == "character.png":
        cogType = cog[4].strip("Name:").lower()+".png"

    stats = ""

    coords = cog[0].strip("Coords:(").strip(")").split(", ")
    x = int(coords[0])
    y = int(coords[1])

    add_html("<img style=\"width:50;height:50;position:absolute;border-style:solid;left:"+str(x*50)+";top:"+str(y*50)+"\" src=\""+cogType+"\"></img>")

    for attr in cog:
        if attr.startswith("Build rate:"):
            add_html("<img style=\"height:16;width:16;position:absolute;left:"+str(x*50)+";top:"+str(y*50)+"\" src=\"buildrate.png\"\"></img>")
            add_html("<p style=\"-webkit-text-fill-color:#ff5500;-webkit-text-stroke:0.3px black;width:16;height:16;font-size:10px;font-family:Arial;position:absolute;left:"+str(x*50+2)+";top:"+str(y*50+6)+"\">"+attr.replace("Build rate:", "")+"</p>")
        elif attr.startswith("Build rate boost:"):
            add_html("<img style=\"height:16;width:16;position:absolute;left:"+str(x*50+16)+";top:"+str(y*50)+"\" src=\"buildrateboost.png\"\"></img>")
            add_html("<p style=\"-webkit-text-fill-color:#00FFFF;-webkit-text-stroke:0.3px black;width:16;height:16;font-size:10px;font-family:Arial;position:absolute;left:"+str(x*50+2+16)+";top:"+str(y*50+6)+"\">"+attr.replace("Build rate boost:", "")+"</p>")
            stats += attr.replace("Build rate boost:", "BRB:")
        elif attr.startswith("Flaggy rate:"):
            add_html("<img style=\"height:16;width:16;position:absolute;left:"+str(x*50+32)+";top:"+str(y*50)+"\" src=\"flaggyrate.png\"\"></img>")
            add_html("<p style=\"-webkit-text-fill-color:#F000F0;-webkit-text-stroke:0.3px black;width:16;height:16;font-size:10px;font-family:Arial;position:absolute;left:"+str(x*50+2+32)+";top:"+str(y*50+6)+"\">"+attr.replace("Flaggy rate:", "")+"</p>")
        elif attr.startswith("Flaggy rate boost:"):
            add_html("<img style=\"height:16;width:16;position:absolute;left:"+str(x*50+34)+";top:"+str(y*50+34)+"\" src=\"flaggyrateboost.png\"\"></img>")
            add_html("<p style=\"-webkit-text-fill-color:#79EC42;-webkit-text-stroke:0.3px black;width:16;height:16;font-size:10px;font-family:Arial;position:absolute;left:"+str(x*50+32)+";top:"+str(y*50+14)+"\">"+attr.replace("Flaggy rate boost:", "")+"</p>")
        elif attr.startswith("Exp mult:"):
            add_html("<img style=\"height:16;width:16;position:absolute;left:"+str(x*50)+";top:"+str(y*50+34)+"\" src=\"expmult.png\"\"></img>")
            add_html("<p style=\"-webkit-text-fill-color:#000000;-webkit-text-stroke:0.3px black;width:16;height:16;font-size:10px;font-family:Arial;position:absolute;left:"+str(x*50)+";top:"+str(y*50+25)+"\">"+attr.replace("Exp mult:", "")+"</p>")
        #    stats += attr.replace("Exp mult:", "XP:")
        #stats += "\n"

    #add_html("<div style=\"color:red;font-size:10px;font-family:Arial;position:absolute;left:"+str(x*50)+";top:"+str(y*50)+";height:50;width:50\">"+stats+"</div>")


add_html("</div>")

#for y in range(8):
#    for x in range(12):
#add_html("""</body>
#</html>""")


#print(output)