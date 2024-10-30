# Databricks notebook source
import pandas as pd
from datetime import datetime

# file path
inputPath = "/Workspace/Users/singhanat.rer@kmutt.ac.th/track_small.csv"
outputPath = "/Workspace/Users/singhanat.rer@kmutt.ac.th/output_small.csv"
testResultPath = "/Workspace/Users/singhanat.rer@kmutt.ac.th/test_result.txt"

# open test result file
f = open(testResultPath, "w")

# read csv file
tracksInput = pd.read_csv(inputPath)
tracksOutput = pd.read_csv(outputPath)

# Case 1
 
if tracksOutput.dtypes["UnitPrice"] == 'int64':
    f.write("Case 1: Passed\n")
else:
    f.write("Case 1: Failed\n")

# Case 2

mergedTracks = tracksInput.merge(tracksOutput, on="TrackId", suffixes=("_input", "_output"))
if (mergedTracks["UnitPrice_output"] - mergedTracks["UnitPrice_input"] < 1).all():
    f.write("Case 2: Passed\n")
else:
    f.write("Case 2: Failed\n")

# close
f.close()
