<?php

$workingver = 2000;

if (isset($_GET['ver']) && htmlentities($_GET['ver']) >= $workingver){
	print 1;
}
else {
	print 0; 
}
