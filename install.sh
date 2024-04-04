#!/bin/bash

# Удалить раздел sda
sfdisk --delete /dev/sda  # это удалит все разделы на sda

# Создать новую таблицу разделов
echo ',+1G,L,*' | sfdisk /dev/sda  # создать раздел для /boot fat32 1GB
echo ',L' | sfdisk /dev/sda  # создать раздел для /

# Форматирование разделов
mkfs.fat -F32 /dev/sda1  # форматирование раздела /boot как fat32
mkfs.ext4 /dev/sda2  # форматирование раздела / как ext4

# Монтирование разделов
mount /dev/sda2 /mnt  # монтирование раздела / во временный каталог /mnt
mkdir /mnt/boot  # создание каталога /boot
mount /dev/sda1 /mnt/boot  # монтирование раздела /boot в /mnt/boot

#Установка ядра
pacstrap -K /mnt base linux linux-firmware

# Настройка системи
genfstab -U /mnt >> /mnt/etc/fstab
pacman -S grub
grub-install --boot-directory=/mnt/boot /dev/sda
arch-chroot /mnt
ln -sf /usr/share/zoneinfo/Ukraine/Kiev /etc/localtime
hwclock --systohc
locale-gen
echo LANG=ru_RU.UTF-8 > /etc/locale.conf
echo python > /etc/hostname
passwd 1234
exit
umount -R /mnt
reboot