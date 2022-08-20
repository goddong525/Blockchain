# 도전과제 2번

from flask import Flask, jsonify, request

app = Flask(__name__)

chain = []

cnt = 0
menu = 0