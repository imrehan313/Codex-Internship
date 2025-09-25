import flask as f
from sentiment import SentimentAnalysis as sa

flask=f.Flask(__name__)
@flask.route("/",methods=["GET","POST"])

def handleSentiment():
    result=None
    text=""

    if f.request.method=="POST":    
        text=f.request.form.get("text")

        result=sa(str(text)).checkSentiment() if text else " "
        text=str(text).title() 

    return f.render_template("sentiment.html",result=result,text=text)

if __name__=="__main__":
    flask.run(debug=True)
