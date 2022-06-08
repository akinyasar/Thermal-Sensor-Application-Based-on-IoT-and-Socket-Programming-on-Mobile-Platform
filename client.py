import socket
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from scipy import interpolate

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12346
# connect to the server on local computer
s.connect(('192.168.50.58', port))

#
#####################################
# Interpolation Properties 
#####################################
#
# original resolution
pix_res = (8,8) # piksel çözünürlüğü
xx,yy = (np.linspace(0,pix_res[0],pix_res[0]),
                    np.linspace(0,pix_res[1],pix_res[1]))
zz = np.zeros(pix_res) 
# yeni çözünürlük
pix_mult = 6 # interpolasyon için çarpan
interp_res = (int(pix_mult*pix_res[0]),int(pix_mult*pix_res[1]))
grid_x,grid_y = (np.linspace(0,pix_res[0],interp_res[0]),
                            np.linspace(0,pix_res[1],interp_res[1]))
# interpolasyon fonksiyonu
def interp(z_var):
    # 8x8 görüntü üzerinde kübik interpolasyon yapılıyor
    f = interpolate.interp2d(xx,yy,z_var,kind='cubic')
    return f(grid_x,grid_y)
grid_z = interp(zz) # interpolasyon edilmiş görüntü
#
#####################################
# Start and Format Figure 
#####################################
#
plt.rcParams.update({'font.size':16})
fig_dims = (10,9) # figure size
fig,ax = plt.subplots(figsize=fig_dims) # start figure
fig.canvas.manager.set_window_title('AMG8833 Image Interpolation')
im1 = ax.imshow(grid_z,vmin=18,vmax=37,cmap=plt.cm.RdBu_r) # plot image, with temperature bounds
cbar = fig.colorbar(im1,fraction=0.0475,pad=0.03) # colorbar
cbar.set_label('Temperature [C]',labelpad=10) # temp. label
fig.canvas.draw() # draw figure

ax_bgnd = fig.canvas.copy_from_bbox(ax.bbox) # background for speeding up runs
fig.show() # show figure


while True:
    data = s.recv(1024).decode('utf-8')
    data = eval(data)
    fig.canvas.restore_region(ax_bgnd) # restore background (speeds up run)
    new_z = interp(np.reshape(data,pix_res)) # interpolated image
    im1.set_data(new_z) # update plot with new interpolated temps
    ax.draw_artist(im1) # draw image again
    fig.canvas.blit(ax.bbox) # blitting - for speeding up run
    fig.canvas.flush_events() # for real-time plot

s.close()