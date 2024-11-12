from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

def prediction(list):
    filenm = 'model\predictor.pickle'
    with open(filenm,'rb') as file :
        model = pickle.load(file)
    pred_value = model.predict([list])
    return pred_value

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/',methods=['POST','GET'])
def index():
    
    
    if request.method == 'POST':
        anex = request.form['range']
        mental = request.form['mental']
        depr = request.form['range2']
        head = request.form['headache']
        bp = request.form['blood_pressure']
        bproblem = request.form['breathing_problem']
        nl = request.form['noise_level']
        sl = request.form['study_load']
        fcc = request.form['future_career_concerns']
        pp = request.form['peer_pressure']
        ea = request.form['extracurricular_activities']
        bull = request.form['bullying']

        feature_list = []
        feature_list.append(anex)
        feature_list.append(mental)
        feature_list.append(depr)
        feature_list.append(head)
        feature_list.append(bp)
        feature_list.append(bproblem)
        feature_list.append(nl)
        feature_list.append(sl)
        feature_list.append(fcc)
        feature_list.append(pp)
        feature_list.append(ea)
        feature_list.append(bull)

        print(feature_list)

        pred = prediction(feature_list)
        #print(pred)
        if pred == 0:
            return render_template("low.html")
        elif pred == 1:
            return render_template("moderate.html")
        else :
            return render_template("high.html")


        
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)