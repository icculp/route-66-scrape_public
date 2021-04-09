sudo apt-get update -y
sudo apt-get install -y chromium-browser=87.0.4280.66-0ubuntu0.16.04.1


sudo apt-get install unzip &&
a=$(uname -m) &&
rm -r /tmp/chromedriver/
mkdir /tmp/chromedriver/ &&
wget -O /tmp/chromedriver/LATEST_RELEASE_87.0.4280 http://chromedriver.storage.googleapis.com/LATEST_RELEASE_87.0.4280 &&
if [ $a == i686 ]; then b=32; elif [ $a == x86_64 ]; then b=64; fi &&
latest=$(cat /tmp/chromedriver/LATEST_RELEASE_87.0.4280) &&
wget -O /tmp/chromedriver/chromedriver.zip 'http://chromedriver.storage.googleapis.com/'$latest'/chromedriver_linux'$b'.zip' &&
sudo unzip /tmp/chromedriver/chromedriver.zip chromedriver -d /usr/local/bin/ &&
echo 'success?'
