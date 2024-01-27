<template>
  <header>
    <h1 id="WebsiteName">Course recommendation</h1>
    <nav class="header_nav">
        <a href="https://www.google.com.tw/" class="linkText">HOME</a>
        <router-link to="/path"><a>LEARNING PATH</a></router-link>
        <router-link to="/course"><a>LEARNING COURSE</a></router-link>
        <router-link to="/history"><a>LEARNING HISTORY</a></router-link>
        <router-link to="/achievement"><a>LEARNING ACHIEVEMENT</a></router-link>
    </nav>
  </header>
  <main>  
    <section id="photo_name"> 
      <div>
        <div class="hello">
          <h1>My Profile</h1>
        </div>
        <img id="photo" src=""/>
        <p>{{formInline.name}}</p>
      </div>
      <div id="profile">
        <table>
        <tr>
          <td>Email</td>
          <td :class="getemail()">{{formInline.mail}}</td>
        </tr>
        <tr>
          <td>department</td>
          <td>{{formInline.dep}}</td>
        </tr>
        <tr>
          <td>Age</td>
          <td>{{formInline.age}}</td>
        </tr>
        <tr>
          <td>Skill</td>
          <td :class="getskill()"><ul><li v-for="sk in formInline.skills" :key="sk">{{ sk }}</li></ul></td>
        </tr>
        </table>
      </div>
    </section>
    <section id="class">
      <h3 id="title">This is our Course recommendation</h3>
      <div id="course">
        <ol>
          <!-- <li id="courseList" v-for="RecomClass in getcourese()" :key="RecomClass">
            <input type="checkbox" value="1" name="Product_1">{{ RecomClass }}
          </li> -->
          <a :class = "getcourse()">{{this.results}}</a>
        </ol> 
        <button type="submit" @click="onSubmitPost"> 提交 </button>
      </div>
    </section>
  </main>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      formInline: {
        Information: '',
        mail:"XXXXXXXXXX@gmail.com",
        name:"Andy",
        dep:"Math",
        age:"21",
        skills: ["Eating", "Coding", "Sleeping", "Reading", "Computing", "drinking", "Eating", "Coding", "Sleeping", "Reading", "Computing", "drinking"],
        recom_class: ["first class", "second class", "third class", "first class", "second class", "third class", "first class", "second class", "third class"]
      },
      results:''
    }
  },
  methods: {
    async getcourse() {
      await axios.get('http://127.0.0.1:8000/courses/recommend_course')
      .then(res => {
        this.results = res.data;
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
      });
      return this.results;
    },
    async getemail() {
      await axios.get('http://127.0.0.1:8000/students/getemail')
      .then(res => {
        this.formInline.mail = res.data;
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
      });
    },
    async getskill() {
      await axios.get('http://127.0.0.1:8000/students/getskill')
      .then(res => {
        this.formInline.skills = res.data.split(', ');
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
      });
    }
  }
}
</script>
<style scoped>
.input {
  width: 200px
}
button {
  width: 100px
}
.textarea {
  width: 900px
}
#inOut{
  margin-top: 62px;
  position: fixed;
}
#course {
  background-color: #ffffff;
} 
#courseList{
  background-color: #ffffff;
  padding: 10px;
}

header {
  background-color: #fff5da;
  width: 90%;
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  left: 5%;
}
main {
  display: flex;
}
.header_nav {
  width: 1000px;
  display: flex;
  padding-right: 10px;
  justify-content: space-between;
}
a {
  text-decoration: none;
  color: #000;
}
#WebsiteName {
  font-size: 30px;
  color: #ca2222;
  text-decoration: underline;
  padding-left: 20px;
}
.linkText:hover {
  transition: all 0.2s;
  color: #FFB500;
}
#photo_name {  
  padding-top: 70px;
  text-align:center;
  width: 25%;
  height: 100%;
  background-color: #30c2ee;
  display: block;
  overflow: auto;
  /*opacity: 0.5;*/
}
#photo{
  border: 5px solid #000;
  text-align:center;
  overflow: hidden;
}
ul {
  padding: 0;
}

#profile {
  width: 100%;
  background-color: #a2fcba;
}
table {
  table-layout: auto;
  width: 100%;
  border: 1px solid red;
  overflow: auto;
  padding: 10px;
}
td {
  padding: 10px;
  border: 1px solid blue;
  overflow: auto;
  white-space: pre-wrap;
  text-overflow: ellipsis;
}
a {
  color: #42b983;
}
#class {
  width: 75%;
  background-color: #ffffff;
}
#classList{
  background-color: #ffffff;
  padding: 10px;
}
#title {
  padding-top: 80px;
  padding-bottom: 10px;
  font-size: larger;
  background-color: #f76c7c;
  margin: 0;
}
#Inform {
  padding-top: 10px;
}
</style>