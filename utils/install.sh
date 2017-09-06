
echo "**********************************************"
echo    " Installing AutoNmap........."
echo "**********************************************"
sleep 3
echo "**********************************************" 
echo " Installting modules via pip..."
echo "**********************************************"
pip install -r requirements.txt
sleep 3

echo "**********************************************"
echo "Creating directories for logs collection"
echo "**********************************************"
cd /
cd home/
rm -rf .autonmap-logs
mkdir .autonmap-logs
cd .autonmap-logs
echo 
mkdir basic/
mkdir SSL/
mkdir SMB/
mkdir TELNET/
mkdir FTP/
mkdir SSH/
mkdir SQLInjection/


echo "**********************************************"
echo " You can now FIRE Up the AutoNmap :):):) "
echo "**********************************************"
sleep 3
cd /
clear
