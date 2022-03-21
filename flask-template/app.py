# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)

# Mekeih Nelson and Teshi
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=['GET','POST'])
def results():
    anwsers = {
    'NY_Capital':[request.form["NY Capital"],'Albany'],
    'CA_Capital':[request.form["CA Capital"],'Sacramento'],
    'MD_Capital':[request.form["MD Capital"],'Annapolis'],
    'AL_Capital':[request.form["AL Capital"],'Juneau'],
    'HI_Capital':[request.form["HI Capital"],'Honolulu']
    }

    return render_template("results.html", eval=anwsers)
