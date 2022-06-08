#!/bin/bash

# Para nuestro caso que necesitamos permisos de superusuario para montar el disco D, ejecutamos el script con `sudo`

# Previamente creamos una carpeta donde se localizara nuestra data (Este paso es evitable y se realiza una sola vez)
# mkdir /media/<user>/DATA/

# Luego montamos el disco D que es el lugar donde estará localizado la data para S2S
# EL nombre de la particion a montar se puede obtener luego de ejecutar `df -h`, para este caso es: "nvme0n1p8"

# Dar permisos recursivos 777 a /media/ y a /dev/nvme0n1p8
# mount /dev/nvme0n1p8 /media/brayan/DATA/  #Primero la ruta de la particion, luego la ruta donde va estar localizado dentro de el sist Linux

export model="NCEP"
export output="/home/brayan/DATA/S2S/raw_data"
export dataset="2m_above_ground"

chmod u+rwx ./url_generator_NCEP.py
./url_generator_NCEP.py

cd "$output/$model/"
sh *txt











# Para desmontar el disco D:

# umount /media/brayan/DATA/



