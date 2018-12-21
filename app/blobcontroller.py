import os,sys
from flask import Flask, render_template, request, redirect
from azure.storage.blob import BlockBlobService, PublicAccess
account_name='krishanstorage'
account_key=<key>
container_name ='test-container'

block_blob_service = BlockBlobService(account_name, account_key)

from init import app

@app.route('/upload', methods=['POST'])
def upload_blob():
    filestream = request.files['myfile']
    block_blob_service.create_blob_from_stream(container_name, filestream.filename, filestream)
    return redirect("/listblobs")

@app.route("/upload", methods=['GET'])
def uploadtoblob():
    return render_template('upload.html', message='Upload  file to blob storage')

@app.route("/listblobs", methods=['GET'])
def  listblobs():
    generator =  block_blob_service.list_blobs(container_name,num_results  = 100)
    return render_template('listblobs.html',blobs = generator)