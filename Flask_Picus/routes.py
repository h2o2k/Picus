# Setting up the various routes so our application knows what data to filter and what links to go to - Andrew

from datetime import datetime # Allows us to set a default time if news articles
import json
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from Flask_Picus import app
from pymongo import MongoClient
from flask_paginate import Pagination, get_page_parameter

client = MongoClient('localhost', 27017)
db = client.BackendDB
collection = db.Articles

@app.route("/")
@app.route("/home")
@app.route("/index") # What we type into browsers to go to various webpages, add extra functions
def index():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find().sort('uploadtime').skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page, total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/local")
def local():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': { '$in': ['BBC Local News', 'Guardian local', 'Reddit local']}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/world")
def world():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': { '$in': ['BBC Global News', 'Guardian world', 'Reddit global']}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/technology")
def technology():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': { '$in': ['BBC Technology News', 'gHacks', 'Guardian']}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/science")
def science():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': { '$in': ['BBC Science News', 'Guardian science', 'Reddit science']}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
        pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/entertainment")
def entertainment():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': { '$in': ['BBC Entertainment News', 'Guardian entertainment', 'Reddit entertainment']}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/bbc")
def bbc():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': {'$regex': '.*BBC'}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/ghacks")
def ghacks():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': 'gHacks'}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/theguardian")
def theguardian():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': {'$regex': '.*Guardian'}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/reddit")
def reddit():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': {'$regex': '.*Reddit'}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)

@app.route("/wired")
def wired():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    articles = collection.find({'author': { "$nin": ["BBC Technology News", "Reddit", "Guardian", "gHacks", "BBC Local News", "BBC Global News", "BBC Science News", "BBC Entertainment News", "Guardian entertainment", "Reddit entertainment", "Guardian science", "Reddit science", "Guardian world", "Reddit global", "Guardian local", "Reddit local", "Guardian technology"]}}).skip((page - 1)*per_page).limit(per_page)
    responses = []
    responses = []
    for article in articles:
        article['_id'] = str(article['_id'])
        responses.append(article)
    pagination = Pagination(page=page,per_page=10 ,total=articles.count(), record_name='articles', css_framework='bootstrap4')
    return render_template('index.html', responses = responses, pagination = pagination)
