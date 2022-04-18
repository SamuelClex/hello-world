import maya.cmds as cmds

if cmds.window('wz_but_win',q=True,ex=True):  
    cmds.deleteUI('wz_but_win')
cmds.window('wz_but_win', width=350,t="STAIRs v1.0" )
cmds.columnLayout('wz_but_win_clay', adjustableColumn=True )
cmds.floatFieldGrp('wz_but_win_fFGA', numberOfFields=1, label='STAIRS COUNT', extraLabel='u')
cmds.floatFieldGrp('wz_but_win_fFGB', numberOfFields=1, label='STAIRS HEIGHT', extraLabel='cm')
cmds.floatFieldGrp('wz_but_win_fFGC', numberOfFields=1, label='STAIRS WIDTH', extraLabel='cm')
cmds.button('wz_but_win_But', label="CREATE",h=40,bgc=(0.1,0.8,0.8),c="wz_sta_main()")
cmds.scrollField('wz_but_win_sF',h=80, editable=False, wordWrap=True, text='')
cmds.showWindow()

def wz_sta_main():   
    a=cmds.floatFieldGrp('wz_but_win_fFGA',q=True,v1=True)    
    h=cmds.floatFieldGrp('wz_but_win_fFGB',q=True,v1=True)
    b=cmds.floatFieldGrp('wz_but_win_fFGC',q=True,v1=True)
    a=int(a)
    for i in range(1,a+1):
        hs=i*h
        cmds.polyCube(w=1,h=hs,d=b,sx=1,sy=1,sz=1,ax=(0,1,0),cuv=4,ch=1)
        M_h=(i-1)*h*0.5
        cmds.move(i,M_h,0,r=1,os=1,wd=1)  
