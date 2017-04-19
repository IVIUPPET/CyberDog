#!/bin/bash

gpio -g mode 18 pwm
gpio pwm-ms
gpio pwmc 192
gpio pwmr 200

gpio -g pwm 18 100
$SHELL
