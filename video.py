# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import streamlit as st
from PIL import Image


# These are the formats supported in Streamlit right now.
VIDEO_EXTENSIONS = ["mp4", "ogv", "m4v", "webm"]

# For sample video files, try the Internet Archive, or download a few samples here:
# http://techslides.com/sample-webm-ogg-and-mp4-video-files-for-html5

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('saint.png')
    # st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.write(' ')
image = Image.open('saint.png')

st.title("Hi Carl!")

st.header("Enjoy your drive!")
st.write(
    "Let start your augmented reality."
)


def get_video_files_in_dir(directory):
    out = []
    for item in os.listdir(directory):
        try:
            name, ext = item.split(".")
        except:
            continue
        if name and ext:
            if ext in VIDEO_EXTENSIONS:
                out.append(item)
    return out


avdir = os.path.expanduser("~")
files = get_video_files_in_dir(avdir)

# if len(files) == 0:
#     st.write(
#         "Put some video files in your home directory (%s) to activate this player."
#         % avdir
#     )

# else:
filename = st.selectbox(
    "Select a Uber type, you want (%s) to drive" % avdir,
    files,
    0,
)

st.video(os.path.join(avdir, filename))
# st.header("Remote video playback")
# st.write("st.video allows a variety of HTML5 supported video links, including YouTube.")


def shorten_vid_option(opt):
    return opt.split("/")[-1]


# A random sampling of videos found around the web.  We should replace
# these with those sourced from the streamlit community if possible!
vidurl = st.selectbox(
    "Pick a video to play",
    (
        "https://youtu.be/_T8LGqJtuGc",
        "https://www.youtube.com/watch?v=kmfC-i9WgH0",
        "https://www.youtube.com/embed/sSn4e1lLVpA",
        "http://www.rochikahn.com/video/videos/zapatillas.mp4",
        "http://www.marmosetcare.com/video/in-the-wild/intro.webm",
        "https://www.orthopedicone.com/u/home-vid-4.mp4",
        "https://www.youtube.com/watch?v=GgxXYqiJsU4",
    ),
    0,
    shorten_vid_option,
)

st.video(vidurl)