# Turn Of fLights At Schedule

### What is this?

This a simple script written in Python who turn off knx lights.

### How can I implement it?

You need two things:
1. A server (virtual or not) running linux with [docker installed](https://docs.docker.com/desktop/linux/install/)
2. Already programmed KNX devices

#### Installation

 1. In your server, clone the repository:
 `git clone https://github.com/kikolouro/TurnOffLightsAtSchedule.git && cd TurnOffLightsAtSchedule`

2. Next build the Image:
`chmod +x build.sh run.sh && ./build.sh`

3. Apply the CronJob configuration ([you can check and generate the schedule here](https://crontab-generator.org/)) Basic one I used is this one:
`20 00 * * * <path>/TurnOffLightsAtSchedule/run.sh <groupaddresses_to_turn_off> >> <output_path>/output.txt 2>&1`
   - <path> is the path for the cloned repository
   - <groupaddresses_to_turn_off> is the group addresses you want to turn of. eg. `1/1/0` (for multiple just use a space in between eg. `1/1/0 1/1/1`)
   - <output_path> is the path of the output file, if you don't want output file use /dev/null

### Roadmap
- [x] Logging, which lights turned off at what schedule
- [ ] Gui for easy configuration

### Want to help?
Just fork the repository and make a pull request. Please use [Convetional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)
GUI development on [TurnOffLightsAtScheduleGUI Repository](https://github.com/kikolouro/TurnOffLightsAtScheduleGUI)
