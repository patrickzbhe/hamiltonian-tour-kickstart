import tkinter
import time

r = tkinter.Tk()
screen = tkinter.Canvas(r, width = 1600, height = 800)
screen.pack()
LOFF = 2
TOFF = 2
BSIZE =20
testn = 2
sample = True
if sample:
    samplen = "sample_"
else:
    samplen = ""
fin = open(f"./{samplen}test_set_{testn}/{samplen}ts{testn}_input.txt", 'r')
f = open("./output.txt", 'r')
#fin = open("./sample_test_set_2/sample_ts2_input.txt", 'r')
#fin = open("./test_set_1/ts1_input.txt", 'r')
fin.readline()
garbage = []

def draw():
    for e in garbage:
        screen.delete(e)
    cline = f.readline()
    r,c = [int(x) for x in fin.readline().strip().split()]
    grid = []
    for _ in range(r):
        grid.append(fin.readline().strip())

    try:
        data = cline.split()[2].strip()
    except:
        return
    
    rr = r * 2
    cc = c * 2
    
    
    for i in range(rr + 1):
        garbage.append(screen.create_line(LOFF, TOFF + i * BSIZE, LOFF + BSIZE * cc, TOFF + i * BSIZE))
    for i in range(cc + 1):
        garbage.append(screen.create_line(LOFF + i * BSIZE, TOFF, LOFF + i * BSIZE, TOFF + BSIZE * rr))
    #print(grid, r, c)
    for row in range(r):
        for col in range(c):
            
            if grid[row][col] != '*':
                basel = LOFF + col * 2 * BSIZE
                baset = TOFF + row * 2 * BSIZE
                garbage.append(screen.create_rectangle(basel, baset, basel+ 2 * BSIZE,baset + 2 * BSIZE, fill='black'))
    cr = 0
    cc = 0
    def convert(row, col):
        return (LOFF + BSIZE//2 + col * BSIZE , TOFF + BSIZE//2 + row * BSIZE )
    if data == "IMPOSSIBLE":
        input()
        return
    for d in data:
        ocr = cr
        occ = cc
        if d == "N":
            cr -= 1
        elif d == "S":
            cr += 1
        elif d == "E":
            cc += 1
        elif d == "W":
            cc -= 1
        else:
            print("?")
        a,b = convert(ocr,occ)
        c,d = convert(cr,cc)
        garbage.append(screen.create_line(a,b,c,d))
    screen.update()
    #time.sleep(0.1)
    input()
while True:
    draw()


r.mainloop()
f.close()