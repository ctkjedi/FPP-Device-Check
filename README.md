# FPP-Device-Check

A python script to run in Falcon Pi Player Scheduler to alert a user, via email, if a show controller is not responding. The email recipient will get an alert message listing the IP address of controller(s) that are not reporting back. IP addresses are gathered from the config on the PI automatically and only report on devices labeled as active.

## Installation

Upload this script using your FPP File Manager

## Usage

Edit the script with the email you'd like to send from, the account password and the email you want alerts sent to. This is structured to use Gmail, so other SMTP information might be required. PLEASE NOTE that Gmail requires a unique App Password to be created for third party usage such as this. You can find more details on this process here: https://forums.raspberrypi.com/viewtopic.php?t=332280 (though some details of the process have changed slightly, but easy to figure out).

Once configured, schedule this to run in FPP or add it to your playlist as you see fit.

## Contributing

Pull requests are welcome. I'm very new to Python and JSON, so this could probably be more streamlined and ripe for improvements. Modify away!

## Additional

Credit to [pcmanbob] for their posts on https://forums.raspberrypi.com/ in passively assisting in this script (i.e., I copied some of their stuff).
