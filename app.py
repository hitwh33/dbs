#!/usr/bin/env python
# coding: utf-8

# In[53]:


from flask import Flask,request,render_template


# In[54]:


import joblib


# In[55]:


app=Flask(__name__)


# In[56]:


__name__


# In[57]:


dir(app)


# In[ ]:





# In[58]:


@app.route("/",methods =["GET","POST"])
def index():
    if request.method=="POST":
        rates= float(request.form.get("rates"))
        model1=joblib.load("regression")
        model2=joblib.load("tree")
        r1=model1.predict([[rates]])
        r2=model2.predict([[rates]])
        return (render_template("frontedge.html",result1=r1,result2=r2))
    else:
        return (render_template("frontedge.html",result1="WAITING",result2="WAITING"))


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[ ]:




