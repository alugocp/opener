if [ "$EUID" != "" ]; then
  echo "You must run this script with root permissions"
  exit
fi

# Create terminal command
mkdir -p ~/bin
cp cli.py ~/bin
mv ~/bin/cli.py ~/bin/opener
chmod +x ~/bin/opener

# Move to Python packages directory
lib=/usr/lib/python2.7/dist-packages/opener
mkdir -p $lib
cp opener.py $lib
mv $lib/opener.py $lib/__init__.py
