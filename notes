goodreads = requests.get("https://www.googleapis.com/books/v1/volumes?q= :isbns" +"&key= :key", params={"key": key, "isbns": result.isbn})
goodreads = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:" +":isbns" + "&jscmd=data&format=json", params={"isbns": result.isbn})
lấy thông tin sách -> lấy key truy cập vô link rating
    goodreads = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:1857231082&jscmd=details&format=json")
link rating
gr = requests.get("https://openlibrary.org/" + goodreads.json()["ISBN:1857231082"]["details"]['works'][0]['key']+ "/ratings.json")

 return render_template("details.html", result=result, comment_list=comment_list , bookid=bookid, goodreads=goodreads.json()["books"][0])

 
 goodreads2 = goodreads = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:1857231082&jscmd=details&format=json")
 key1 = goodreads2.json()["ISBN:1857231082"]["details"]['works'][0]['key']
 goodreads3 = requests.get("https://openlibrary.org/" + key1 + "/ratings.json").json()
 goodreads_book = goodreads3["summary"]