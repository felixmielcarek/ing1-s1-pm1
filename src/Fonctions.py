#Librairie crée par Micael FEBRAS FRAGOSO CARMONA

import dash
from dash import html,dcc,dash_table
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
from dash import html, dcc, Output, Input,State, ctx
import dash_bootstrap_components as dbc
import base64
import io
import json
from datetime import datetime
import numpy as np
from dash import no_update
from dash.exceptions import PreventUpdate
from scipy.optimize import curve_fit
from scipy.special import factorial
import os
import importlib.util
import subprocess
import re
import inspect
import shutil
import sys
from front_end import app_layout
import modin.config as cfg
from dask.distributed import Client
import multiprocessing
import socket
import time
from docx import Document
import glob
import pandas as pd


