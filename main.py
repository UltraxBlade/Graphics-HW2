from display import *
from draw import *
from matrix import *


m2=[]
print("Testing add_edge. m2 =")
print_matrix(m2)
print("(That was empty.) Adding (1, 2, 3), (4, 5, 6). m2 =")
add_edge(m2,1,2,3,4,5,6)
print_matrix(m2)
m1=ident(new_matrix())
print("Testing ident. m1 =")
print_matrix(m1)
print("Testing matrix_mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)
print("Reassigning m1. m1 =")
m1=[[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]
print_matrix(m1)
print("Testing matrix_mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)

def translate(edges,dr,dc,dz):
    newEdges=[]
    for col in range(len(edges)):
        add_point(newEdges,int(edges[col][0]+dr),int(edges[col][1]+dc),int(edges[col][2]+dz))        
    return newEdges

def dilate(edges,dr,dc,dz):
    newEdges=[]
    for col in range(len(edges)):
        add_point(newEdges,int(edges[col][0]*dr),int(edges[col][1]*dc),int(edges[col][2]*dz))        
    return newEdges

img = new_screen()
edges = new_matrix()
#chin
add_edge(edges,400,230,0,400,270,0)
add_edge(edges,400,230,0,300,200,0)
add_edge(edges,400,270,0,300,300,0)
add_edge(edges,400,230,0,390,240,0)
add_edge(edges,400,270,0,390,260,0)
add_edge(edges,390,240,0,390,260,0)
#mouth
add_edge(edges,300,200,0,305,190,0)
add_edge(edges,300,300,0,305,310,0)
add_edge(edges,300,200,0,300,300,0)
add_edge(edges,305,190,0,240,185,0)
add_edge(edges,305,310,0,240,315,0)
add_edge(edges,263,204,0,263,296,0)
add_edge(edges,282,206,0,242,203,0)
add_edge(edges,282,294,0,242,297,0)
add_edge(edges,282,294,0,282,206,0)
add_edge(edges,282,224,0,245,222,0)
add_edge(edges,282,241,0,247,239,0)
add_edge(edges,282,259,0,247,261,0)
add_edge(edges,282,276,0,245,278,0)
#nose
add_edge(edges,225,240,0,255,250,0)
add_edge(edges,225,260,0,255,250,0)
add_edge(edges,225,240,0,215,230,0)
add_edge(edges,225,260,0,215,270,0)
add_edge(edges,185,250,0,215,230,0)
add_edge(edges,185,250,0,215,270,0)
#moustache
add_edge(edges,215,230,0,200,130,0)
add_edge(edges,215,270,0,200,370,0)
add_edge(edges,249,248,0,226,100,0)
add_edge(edges,249,252,0,226,400,0)
add_edge(edges,80,90,0,226,100,0)
add_edge(edges,80,410,0,226,400,0)
add_edge(edges,80,90,0,200,130,0)
add_edge(edges,80,410,0,200,370,0)
#eyes
add_edge(edges,206,175,0,130,170,0)
add_edge(edges,206,325,0,130,330,0)
add_edge(edges,200,185,0,200,235,0)
add_edge(edges,200,265,0,200,315,0)
add_edge(edges,200,185,0,155,185,0)
add_edge(edges,155,315,0,200,315,0)
add_edge(edges,200,235,0,180,235,0)
add_edge(edges,200,265,0,180,265,0)
add_edge(edges,150,175,0,180,235,0)
add_edge(edges,150,325,0,180,265,0)
add_edge(edges,150,175,0,135,180,0)
add_edge(edges,150,325,0,135,320,0)
add_edge(edges,165,240,0,180,235,0)
add_edge(edges,165,260,0,180,265,0)
add_edge(edges,165,240,0,135,180,0)
add_edge(edges,165,260,0,135,320,0)
add_edge(edges,200,220,0,173,220,0)
add_edge(edges,200,280,0,173,280,0)
#ears
add_edge(edges,155,171,0,120,125,0)
add_edge(edges,195,174,0,120,125,0)
add_edge(edges,155,329,0,120,375,0)
add_edge(edges,195,326,0,120,375,0)
#hat
add_edge(edges,130,170,0,120,220,0)
add_edge(edges,130,330,0,120,280,0)
add_edge(edges,130,170,0,140,220,0)
add_edge(edges,130,330,0,140,280,0)
add_edge(edges,120,220,0,120,280,0)
add_edge(edges,140,220,0,140,280,0)
add_edge(edges,130,170,0,110,150,0)
add_edge(edges,130,330,0,110,350,0)
add_edge(edges,110,150,0,90,150,0)
add_edge(edges,110,350,0,90,350,0)
add_edge(edges,90,150,0,40,200,0)
add_edge(edges,90,350,0,40,300,0)
add_edge(edges,40,200,0,40,300,0)
add_edge(edges,120,230,0,110,220,0)
add_edge(edges,120,270,0,110,280,0)
add_edge(edges,110,220,0,90,220,0)
add_edge(edges,110,280,0,90,280,0)
add_edge(edges,90,220,0,75,235,0)
add_edge(edges,90,280,0,75,265,0)
add_edge(edges,75,235,0,75,265,0)
add_edge(edges,117,237,0,85,237,0)
add_edge(edges,117,247,0,95,247,0)
add_edge(edges,117,247,0,117,237,0)
add_edge(edges,85,237,0,85,263,0)
add_edge(edges,95,247,0,95,263,0)
add_edge(edges,85,263,0,95,263,0)
#0.25
color2=[175,0,255]
edges2=dilate(edges,0.25,0.25,0.25)
draw_lines(edges2,img,color2)
edges21=translate(dilate(edges2,-1,1,1),500,0,0)
draw_lines(edges21,img,color2)
edges22=translate(dilate(edges2,1,-1,1),0,500,0)
draw_lines(edges22,img,color2)
edges23=translate(dilate(edges2,-1,-1,1),500,500,0)
draw_lines(edges23,img,color2)
#0.5
color3=[255,255,0]
edges3=dilate(edges,0.5,0.5,0.5)
draw_lines(edges3,img,color3)
edges31=translate(dilate(edges3,-1,1,1),500,0,0)
draw_lines(edges31,img,color3)
edges32=translate(dilate(edges3,1,-1,1),0,500,0)
draw_lines(edges32,img,color3)
edges33=translate(dilate(edges3,-1,-1,1),500,500,0)
draw_lines(edges33,img,color3)
#0.75
color4=[175,0,255]
edges4=dilate(edges,0.75,0.75,0.75)
draw_lines(edges4,img,color4)
edges41=translate(dilate(edges4,-1,1,1),500,0,0)
draw_lines(edges41,img,color4)
edges42=translate(dilate(edges4,1,-1,1),0,500,0)
draw_lines(edges42,img,color4)
edges43=translate(dilate(edges4,-1,-1,1),500,500,0)
draw_lines(edges43,img,color4)
#1
color1=[255,255,0]
draw_lines(edges,img,color1)
#display(screen)
save_ppm(img,"image.ppm")



