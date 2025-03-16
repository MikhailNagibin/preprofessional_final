import requests
from flask import *
# from our_requests import *
from forms import *
import matplotlib.pyplot as plt
import numpy as np


data = [[255,255,255,22,22,24,27,31,37,44,54,63,68,74,83,88,88,87,83,78,73,66,57,49,42,35,29,24,19,17,15,12,11,10,11,12,12,13,13,14,14,15,15,16,16,17,16,15,12,10,8,6,5,5,6,8,11,15,20,25,32,39,47,56],[255,255,255,24,24,26,29,33,39,47,56,64,68,72,80,85,85,84,81,77,73,66,57,49,41,33,27,22,18,16,14,13,11,11,12,13,14,15,15,17,18,19,20,20,21,22,21,19,16,13,11,9,8,7,8,11,15,19,24,30,37,43,50,58],[255,255,255,27,28,29,32,36,42,50,59,67,69,71,77,83,83,82,80,77,73,68,58,49,41,33,27,22,18,16,15,13,12,12,13,14,15,17,18,20,22,24,25,26,28,29,27,26,22,18,15,12,11,10,11,14,18,23,28,34,40,46,52,59],[255,255,255,30,31,32,35,39,45,52,61,67,67,68,72,77,76,76,75,73,71,66,56,48,40,32,26,21,17,16,15,14,13,13,14,15,17,18,20,23,26,29,32,34,36,38,37,35,31,26,21,18,15,15,16,19,23,28,33,38,44,49,54,60],[255,255,255,36,37,38,40,44,49,56,63,67,66,64,67,70,69,69,69,67,66,61,53,45,38,31,26,21,17,16,16,15,14,14,15,16,18,20,23,27,31,35,39,42,46,50,49,47,41,35,30,25,22,20,21,24,29,33,38,43,48,52,56,62],[255,255,255,43,44,45,48,51,56,62,68,71,69,66,67,70,69,68,67,65,64,60,52,44,37,30,26,21,17,17,16,15,14,15,16,17,19,22,25,30,36,41,46,51,57,62,61,59,53,46,39,33,29,27,27,30,34,38,43,46,51,53,57,62],[255,255,255,54,55,56,58,61,66,72,77,79,75,70,71,72,70,69,68,66,64,60,52,44,37,30,25,21,17,17,16,15,14,14,15,17,19,21,25,30,37,43,50,56,64,70,71,69,63,56,48,41,36,33,33,35,39,42,46,49,53,54,57,63],[255,255,255,70,70,71,73,75,80,85,89,90,84,78,76,76,73,70,68,65,63,59,50,43,36,29,24,19,16,15,15,14,13,13,14,15,17,19,23,28,36,43,51,58,67,74,75,74,69,62,55,47,42,39,38,39,42,45,48,50,53,54,57,62],[255,255,255,83,84,84,86,87,91,97,101,101,93,86,83,81,75,70,66,62,59,54,46,38,32,25,20,16,13,13,13,12,11,11,12,13,14,16,20,26,33,41,50,57,67,75,77,76,72,67,59,52,47,43,42,42,44,45,48,49,51,52,53,57],[255,255,255,95,95,95,96,97,101,108,112,112,102,94,89,85,78,70,64,58,54,48,40,32,26,20,16,12,10,10,10,9,8,8,9,10,12,13,16,22,29,36,44,52,61,70,72,73,70,65,58,52,47,44,42,42,43,44,46,46,48,48,48,52],[255,255,255,104,105,104,105,107,113,122,126,125,114,104,98,92,82,72,64,55,49,43,35,27,21,15,12,9,7,7,7,7,6,6,7,8,9,11,14,18,25,32,40,47,56,65,67,68,66,62,57,51,46,43,42,43,44,44,46,46,47,46,47,50],[255,255,255,109,110,110,112,115,123,132,136,135,123,112,103,95,83,72,61,52,44,36,28,21,16,11,8,6,5,5,5,5,4,5,5,6,7,9,12,17,23,30,38,45,54,63,66,66,65,61,55,50,45,43,42,42,43,44,45,45,47,46,46,49],[255,255,255,104,105,106,110,114,121,130,134,132,120,109,99,90,78,66,55,45,37,30,22,16,12,8,5,4,3,3,4,3,4,4,4,5,7,9,12,17,24,31,39,47,57,65,67,66,63,58,53,47,43,41,39,39,40,42,44,44,45,45,46,50],[255,255,255,93,95,95,99,103,109,116,118,116,105,95,85,76,65,54,45,36,29,23,17,12,9,6,4,3,2,3,3,3,3,3,4,5,7,9,12,18,25,33,42,50,59,67,67,65,61,56,50,45,41,38,36,36,37,39,42,43,45,45,47,53],[255,255,255,87,88,88,90,94,100,106,106,103,93,82,73,63,53,43,35,27,22,17,13,9,6,4,3,2,2,2,2,3,3,3,4,5,7,9,13,19,26,35,44,52,61,68,68,65,60,54,48,42,38,35,33,33,34,36,39,41,44,46,49,57],[255,255,255,79,80,80,82,85,90,96,96,91,82,72,63,54,45,36,28,21,17,12,9,7,5,3,2,2,2,2,2,3,3,4,4,5,7,10,14,20,28,37,46,54,62,68,66,62,57,51,44,39,35,31,29,29,29,31,35,38,41,43,48,57],[255,255,255,73,75,74,76,78,82,87,86,81,72,63,54,46,37,29,22,17,13,9,7,5,4,3,2,2,2,2,2,3,3,4,5,6,8,10,15,21,29,38,47,55,62,67,64,59,53,46,40,35,31,28,25,25,25,27,31,34,37,40,46,56],[255,255,255,68,70,69,71,72,76,79,78,73,65,57,48,39,31,24,18,13,10,7,5,4,3,2,2,1,1,2,2,3,4,4,5,6,8,11,16,22,30,38,46,53,59,62,58,52,45,39,33,29,25,23,20,20,20,22,26,29,33,36,41,50],[255,255,255,57,59,59,60,61,64,67,66,62,56,49,41,34,26,20,15,10,8,6,4,3,3,2,2,2,2,2,3,3,4,5,6,7,9,12,16,22,28,36,42,47,52,53,49,42,36,30,25,22,19,17,16,16,16,18,22,25,28,30,35,43],[255,255,255,51,53,53,53,54,56,58,57,54,49,43,37,29,22,16,12,8,6,4,3,3,3,2,2,2,2,2,3,4,5,6,7,8,9,12,15,20,25,31,36,40,43,43,39,33,27,23,19,16,15,13,12,12,13,15,18,21,23,25,30,36],[255,255,255,48,50,50,50,50,51,54,53,50,46,40,34,27,20,15,11,7,5,4,3,3,2,2,2,2,2,3,3,4,5,6,7,8,9,11,14,18,23,27,31,34,35,35,30,25,20,17,14,12,11,10,9,9,10,11,14,17,19,21,24,30],[255,255,255,46,47,47,46,46,47,49,48,45,42,37,31,25,18,13,10,7,6,4,4,4,3,3,3,3,3,4,4,5,7,8,8,9,9,11,13,17,20,24,26,28,29,28,24,19,15,12,10,9,8,8,7,7,8,9,12,14,15,17,20,24],[255,255,255,47,48,47,45,44,44,45,43,41,37,33,27,22,16,12,9,7,6,5,5,5,5,5,4,5,5,6,6,8,9,10,10,10,10,11,12,15,17,20,22,23,23,22,18,14,11,8,7,6,6,6,5,6,6,8,10,11,13,14,16,20],[255,255,255,47,48,46,44,41,40,40,38,36,33,29,24,19,14,11,9,7,7,6,6,7,8,8,7,8,8,8,9,11,12,12,12,11,11,11,12,14,15,17,19,19,18,17,14,10,7,6,5,4,4,4,4,5,5,6,8,10,11,12,14,16],[255,255,255,49,50,47,44,40,38,36,34,32,30,27,22,18,14,11,9,8,8,8,9,11,11,12,12,12,12,12,14,15,16,17,16,14,13,13,13,14,15,17,17,17,17,15,12,8,6,4,4,3,3,3,3,4,4,5,7,8,9,10,12,14],[255,255,255,53,54,50,46,41,37,34,31,29,28,24,20,16,13,10,9,8,9,10,12,15,16,17,17,18,17,18,20,21,23,23,21,18,17,17,17,17,18,18,19,19,18,15,12,8,5,4,3,3,3,3,3,3,4,5,6,7,8,9,11,13],[255,255,255,54,54,51,45,39,34,31,28,26,25,22,19,15,12,11,10,10,11,13,16,20,23,24,25,25,24,25,26,28,29,29,27,24,22,21,21,21,21,22,23,22,21,18,13,9,6,4,3,3,3,3,3,3,3,4,5,6,7,8,10,12],[255,255,255,55,55,51,44,38,32,28,25,23,23,21,18,15,12,11,11,12,14,17,21,27,32,34,35,34,34,34,36,37,39,38,34,31,28,27,26,26,27,27,27,26,24,20,15,10,7,5,4,3,3,3,2,2,2,3,4,4,5,6,7,10],[255,255,255,59,59,55,48,40,33,29,26,25,24,23,20,17,14,14,14,15,19,23,29,37,42,46,48,47,46,46,48,49,50,48,44,39,35,33,32,31,31,31,31,29,26,22,16,11,7,5,4,3,3,2,2,2,2,2,2,3,3,4,5,7],[255,255,255,66,65,61,52,44,37,31,29,28,28,27,24,21,18,18,19,20,25,31,38,49,55,59,62,61,60,60,60,61,61,58,53,46,42,39,36,35,34,33,32,30,26,22,16,11,7,5,4,3,2,2,1,1,1,1,1,1,1,2,3,5],[255,255,255,73,72,68,59,50,42,36,33,32,33,32,30,27,24,23,24,26,32,38,47,58,65,70,73,73,72,72,72,71,70,66,59,52,47,43,41,39,37,36,34,31,27,21,16,11,7,5,3,2,2,1,1,1,0,0,0,0,0,1,1,2],[255,255,255,77,76,72,63,55,46,40,37,37,38,38,36,33,30,30,31,34,41,48,57,69,76,81,85,86,85,84,83,81,78,73,65,58,52,48,45,43,40,38,35,32,27,21,16,11,8,5,4,2,2,1,1,0,0,0,0,0,0,0,1,1],[255,255,255,77,76,73,65,57,49,43,40,40,43,44,42,40,38,38,39,43,51,60,69,82,90,95,100,100,99,97,95,91,87,80,72,64,58,53,50,47,44,41,38,34,28,23,18,13,9,7,5,3,2,1,1,0,0,0,0,0,0,0,0,1],[255,255,255,78,77,73,66,59,52,45,44,45,49,51,51,49,47,48,50,54,63,73,84,96,104,108,114,115,113,110,106,100,95,88,79,71,65,60,56,53,50,47,43,38,32,26,21,16,12,9,7,5,3,2,1,1,0,0,0,0,0,0,0,0],[255,255,255,74,73,70,63,58,52,47,47,49,55,58,60,59,58,59,62,68,78,88,99,112,120,124,130,131,130,126,120,113,106,98,89,81,74,69,66,62,59,55,51,45,38,31,26,21,17,13,10,8,5,4,2,1,0,0,0,0,0,0,0,0],[255,255,255,66,65,63,57,54,49,46,47,50,57,63,66,67,68,71,75,82,93,103,114,126,133,137,143,144,143,138,131,123,115,106,98,90,84,80,78,75,73,69,63,56,48,41,35,29,25,21,17,13,9,6,4,2,1,0,0,0,0,0,0,0],[255,255,255,54,53,52,48,46,44,42,44,49,58,65,71,75,78,83,89,97,109,119,130,141,146,148,154,155,152,146,139,130,122,113,106,100,96,94,94,93,91,87,82,73,64,56,49,42,37,31,26,20,15,10,7,4,3,2,1,1,0,0,0,0],[255,255,255,41,41,41,39,39,38,38,42,49,59,69,78,85,90,98,104,114,127,138,147,156,160,161,166,167,164,158,151,142,134,126,119,115,113,114,115,116,115,111,105,95,84,75,66,59,52,46,39,31,24,17,12,9,6,4,3,2,2,2,1,1],[255,255,255,31,31,32,32,33,34,36,42,51,62,75,87,97,104,113,120,130,141,150,156,162,164,164,168,169,167,161,155,147,140,135,132,131,131,135,139,141,142,138,131,119,107,97,87,79,71,63,55,45,35,27,20,15,11,8,7,5,4,4,3,3],[255,255,255,22,23,24,25,28,30,33,40,50,64,79,93,104,112,121,128,137,146,151,152,155,154,154,158,159,157,153,149,144,141,140,140,143,147,153,159,165,168,164,156,143,130,118,108,99,89,80,71,59,48,38,30,23,18,14,12,10,8,7,6,5],[255,255,255,16,17,19,20,24,27,31,40,51,66,81,96,108,116,125,131,138,144,144,142,141,139,138,142,143,144,143,142,140,141,143,147,153,160,169,177,185,190,186,177,163,150,138,128,119,109,100,90,77,64,52,43,35,28,23,20,17,14,12,10,8],[255,255,255,11,12,14,16,20,24,29,38,50,65,81,97,109,116,125,130,136,138,135,131,127,124,123,126,129,131,132,133,133,134,140,145,153,162,171,179,187,193,189,181,168,155,146,139,130,122,115,105,91,78,66,57,48,40,34,30,26,22,18,15,12],[255,255,255,8,8,11,13,17,22,28,38,50,66,83,100,112,120,129,132,136,135,130,123,117,113,110,114,117,119,120,122,122,125,131,138,146,155,163,170,175,182,179,171,159,150,143,139,132,126,122,115,103,91,80,72,63,55,47,42,38,32,26,21,16],[255,255,255,6,7,9,11,16,21,27,38,51,67,84,102,115,124,131,134,136,134,127,117,110,105,103,106,109,112,113,117,118,120,126,133,142,150,156,161,164,168,165,158,147,140,136,133,128,124,123,119,111,102,93,86,79,72,63,57,50,42,34,27,21],[255,255,255,5,6,7,10,14,19,26,36,49,65,82,100,113,123,130,133,132,129,121,112,104,98,96,98,101,104,105,109,110,112,118,124,132,140,145,147,148,150,146,139,131,125,122,120,116,114,116,116,110,105,99,95,91,85,76,69,62,52,42,33,25],[255,255,255,4,4,6,8,11,16,23,33,45,61,77,94,108,118,126,128,126,122,114,106,98,93,90,91,93,96,98,102,103,104,109,115,122,129,134,133,132,132,127,120,112,107,105,103,100,99,104,107,105,103,101,100,99,95,88,81,73,62,50,39,30],[255,255,255,3,3,5,6,9,14,20,30,42,57,73,90,104,115,122,124,121,117,109,101,95,90,87,88,89,92,94,98,98,99,103,107,113,119,121,119,115,113,108,101,94,90,88,87,84,85,91,96,98,99,100,103,104,102,96,89,82,70,57,45,34],[255,255,255,2,3,4,5,8,12,18,28,39,54,70,87,102,113,121,122,118,114,106,99,93,89,87,86,87,88,89,92,92,92,95,98,103,108,108,103,98,94,89,83,77,73,72,71,69,71,77,82,86,89,93,97,101,101,96,90,83,71,58,46,36],[255,255,255,2,3,4,5,7,11,16,26,37,52,67,84,99,110,118,118,114,109,103,95,90,87,87,86,86,86,86,89,88,88,89,91,95,98,96,90,83,79,73,67,62,58,57,57,55,55,61,66,70,75,80,86,90,92,88,83,77,66,55,44,35],[255,255,255,2,3,4,5,7,11,17,26,38,52,68,85,100,111,118,116,111,106,99,93,88,85,85,84,83,82,82,84,82,82,83,83,87,89,85,77,70,64,58,52,47,44,43,42,40,40,44,49,53,58,63,70,75,78,76,73,68,59,49,40,32],[255,255,255,3,3,4,6,8,11,17,27,39,53,69,86,101,111,116,113,106,101,95,89,85,83,83,82,81,79,78,80,79,78,79,80,83,84,79,69,61,54,48,42,37,34,32,31,29,28,31,34,38,43,48,54,60,63,63,62,58,51,43,36,29],[255,255,255,4,4,6,7,10,13,19,29,41,56,72,89,103,113,118,113,105,99,94,88,85,83,83,82,80,78,76,78,77,76,76,76,79,79,73,63,53,46,39,33,29,25,24,23,20,19,20,23,25,29,34,39,45,49,50,50,49,44,38,33,28],[255,255,255,6,7,9,11,13,17,24,35,48,65,82,100,113,122,125,119,108,102,95,90,87,85,85,83,80,76,75,76,74,73,72,72,74,74,67,56,46,38,32,26,22,19,17,16,13,12,13,14,16,19,23,28,33,37,39,41,41,38,34,30,27],[255,255,255,10,11,13,15,18,22,30,42,57,75,94,112,125,132,134,126,113,105,99,92,90,88,89,86,81,77,76,77,74,72,71,71,73,72,65,54,43,35,28,22,18,16,14,11,9,8,8,9,10,12,15,18,22,26,28,30,31,30,28,26,24],[255,255,255,14,15,17,20,23,27,35,49,66,85,104,124,136,142,143,134,120,111,104,98,95,94,93,89,83,78,75,75,72,69,68,67,68,67,60,49,40,32,25,20,16,13,11,9,7,6,6,6,6,7,9,11,14,17,19,21,23,23,22,21,21],[255,255,255,17,18,20,22,25,30,39,53,70,90,110,130,143,150,151,142,128,118,110,104,102,99,97,92,84,77,73,72,68,65,63,61,62,61,55,45,36,29,23,18,15,12,10,8,5,4,4,4,4,5,6,7,9,11,12,14,16,17,17,18,18],[255,255,255,18,19,21,23,26,30,38,53,70,89,110,131,145,153,155,148,134,125,118,112,110,107,104,96,86,77,72,69,64,60,57,54,55,54,50,42,34,28,23,18,15,12,10,8,5,4,3,3,3,3,4,4,6,7,8,10,11,13,14,15,16],[255,255,255,19,20,21,23,25,29,36,49,65,85,106,127,142,151,156,150,137,129,123,117,114,110,106,97,85,73,66,61,55,51,47,45,46,46,43,38,32,27,23,19,15,13,11,8,5,4,3,2,2,2,2,2,3,4,5,6,7,9,10,12,14],[255,255,255,19,20,21,22,24,27,33,45,60,78,98,118,133,142,147,142,130,123,118,112,108,103,98,89,76,64,57,51,45,41,38,37,38,40,38,35,31,27,24,20,17,15,13,9,6,5,3,2,2,1,1,1,2,2,3,4,5,6,7,9,12],[255,255,255,18,19,20,21,22,24,30,40,53,70,87,104,117,125,130,126,116,110,105,99,95,91,86,76,65,53,46,41,36,32,30,29,31,34,34,33,31,28,26,23,21,18,16,12,9,6,4,3,2,2,1,1,1,1,2,2,3,4,5,7,9],[255,255,255,17,18,18,19,20,22,26,36,47,62,78,94,105,112,117,114,105,99,93,88,84,79,74,64,53,42,35,30,26,24,22,22,24,27,29,30,30,29,28,26,24,22,20,16,12,10,7,5,3,2,2,1,1,1,1,2,3,4,5,6,8],[255,255,255,15,15,16,17,18,19,23,32,42,56,71,86,97,103,108,105,98,92,86,80,75,70,63,54,43,33,26,22,19,17,16,17,19,23,26,28,29,31,32,31,30,29,28,24,19,16,12,9,6,4,3,2,2,1,2,2,3,4,5,6,8],[255,255,255,11,12,13,13,14,15,19,26,35,48,61,75,86,92,96,95,90,85,78,72,66,60,54,45,34,25,19,16,13,11,11,12,15,18,22,25,29,31,34,35,36,37,37,33,28,24,19,15,11,7,5,3,3,2,2,2,3,4,5,6,8],[255,255,255,8,9,9,10,11,13,16,22,31,43,55,69,80,86,91,90,85,80,73,66,59,53,46,37,27,19,14,11,9,7,7,9,11,15,19,24,29,33,38,41,44,46,48,45,40,35,30,24,18,13,9,6,5,4,3,3,4,5,5,7,9]]

def make_map(data):
    data_array = np.array(data)
    plt.imshow(data_array, cmap='binary')
    plt.colorbar(label='Высоты')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('static/default_map.png', dpi=300, bbox_inches='tight')
    return




app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# @app.route('/')
# def index():
#     return render_template("map_blank.html")


@app.route('/')
def input_link():
    form = InputlinkForm()
    if request.method == "POST":
        return redirect('/input_link')
    return render_template("input_link.html", form=form, active_page="input_link")


IMAGES = {
    "base_stations": "default_map.png",
    "station_radii": "rad_map.png",
    "research_stations": "static/res_map.png"
}

@app.route('/map_blank', methods=["GET", "POST"])
def map_blank():
    current_image = "default-image-6.jpg"
    form = MapviewForm()
    if request.method == "POST":
        button_clicked = request.form.get("action")
        if button_clicked in IMAGES:
            current_image = IMAGES[button_clicked]
    return render_template("map_blank.html", active_page="map_blank", current_image=current_image, form=form)


if __name__ == "__main__":
    # conn = get_db_connection()
    # cur = conn.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)