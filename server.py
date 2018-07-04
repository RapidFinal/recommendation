from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/getRecommendation')
def getRecommendation():
    if 'uid' in request.args:
        uid = request.args.get('uid')
        return render_template(uid)
    else:
        return "No uid specified"

if __name__=='__main__':
    app.run(debug=True)
