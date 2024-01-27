<!--
<template>
  <el-form :inline="true" :model="formInline" size="small" >
    <el-form-item label="用户信息555">
      <el-input class="input" v-model="formInline.username" placeholder="用户名"></el-input>
      <el-input class="input" v-model="formInline.email" placeholder="email"></el-input>
    </el-form-item>
   <el-form-item>
      <el-button type="primary" @click="onSubmitGet">get 查询所有</el-button>
      <el-button type="primary" @click="onSubmitPost">post 提交</el-button>
    </el-form-item>
   <el-input type="textarea" :rows="6" placeholder="此处返回结果" v-model="results" class="textarea"> </el-input>
  </el-form>
  
  
  </template>
  <script>
    import axios from 'axios'
    export default {
      data() {
        return {
          formInline: {
            username: '',
            email: '',
          },
          results:''
        }
      },
      methods: {
        onSubmitGet() {
          console.log('submit! get');
            axios.get('http://127.0.0.1:8000/users/', this.formInline).then(res => {
            this.results = JSON.stringify(res.data);
            console.log(res.data);
          }).catch(() => {
            alert('wrong');
          })
  
  
        },
        onSubmitPost() {
          console.log('submit! post');
            axios.post('http://127.0.0.1:8000/users/', this.formInline).then(res => {
            console.log(res.data);
          }).catch(() => {
            alert('wrong');
          })
  
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
</style>
-->
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
          <td>{{formInline.mail}}</td>
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
          <td><ul><li v-for="sk in formInline.skills" :key="sk">{{ sk }}</li></ul></td>
        </tr>
        </table>
      </div>
      
    </section>
  
    <section id="class">
      <h3 id="title">The record of learning</h3>
      <ol>
        <li id="classList" v-for="Lclass in formInline.learned_class" :key="Lclass">{{ Lclass }}</li>
      </ol>
    <!--
      <form id="Inform" >
        <label for="email">email</label>
        <input id="email" type="text" v-model="email" />
      </form>
      <button id="btn">Save</button>
    
      
      <el-form id="Inform" :inline="true" :model="formInline" size="small"  >
        <el-form-item label="Please input">
          <el-input class="input" v-model="formInline.Information" placeholder="Information"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmitPost">post 提交</el-button>
        </el-form-item>
        <el-input type="textarea" :rows="10" placeholder="此处返回结果" v-model="results" class="textarea"> </el-input>
      </el-form>
    -->
    </section>
    
  </main>
  
  <footer>

  </footer>
</template>

<script>
import axios from 'axios';

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
            learned_class: ["first class", "second class", "third class", "first class", "second class", "third class", "first class", "second class", "third class"]
          },
          results:''
        }
      },
      methods: {
        getPhoto() {
          axios.get('http://127.0.0.1:8000/students/printUser/', this.formInline)
          .then(res => {
            this.results = JSON.stringify(res.data);
            if (res.data == 'failed')
              alert('Invalid Username or Password');
            console.log(res.data);
          })
          .catch(error => {
            console.error('Error:', error);
            alert('An error occurred');
          });
          this.results = '\'' + this.results + '\''
          return this.results;
        }
      }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

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
  background-color:  #FFB500;
  margin: 0;
}
/*
.input {
  width: 300px;
}
button {
  width: 100px
}
.textarea {
  width: 900px
}
*/
#Inform {
  padding-top: 10px;
}

</style>
