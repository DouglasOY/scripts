# get the audio, video duration.
mplayer.exe -vo null -ao null -frames 0 -identify *.(mp3|mp4|avi| wma|swf|...) | grep  "ID_LENGTH="

# the double quote is essential.
while read line ; do   mplayer.exe -vo null -ao null -frames 0 -identify  "${line}"  | grep "ID_LENGTH" ; done < list    >> durations

# 
astyle --style=linux  --indent=spaces=4 -f -p -U  -n  send.c
astyle --style=ansi --indent=spaces=4 --indent-switches --pad-oper --pad-header --add-brackets --suffix=none receive.c 

#
find  . -mindepth 1 -maxdepth 1 -type d | grep -v git | xargs -n 1 -I "ZZZ" du -sh "ZZZ"


QEMU:


debootstrap focal /mnt/focal_rootfs http://archive.ubuntu.com/ubuntu/

chroot  focal_rootfs
useradd firstuser
adduser firstuer sudo
exit

dd if=/dev/zero of=focal_v3_rootfs bs=1M count=1024
mkfs.ext4  focal_v3_rootfs
mount -o loop  focal_v3_rootfs  test/ 
cp -a  focal_rootfs/*  test/ 
umount test/

qemu-system-x86_64 -kernel vmlinux -initrd initrd.img  -append "console=ttyS0 root=/dev/sda" -nographic -m 2048 -hda /mnt/focal_v3_rootfs    



