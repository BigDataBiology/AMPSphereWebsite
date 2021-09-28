<template>
  <div id="Contact">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/contact' }">Contact</el-breadcrumb-item>
        </el-breadcrumb>

        <h1>Contact</h1>
        <p>AMPsphere also is discussed in a forum where users can suggest improvements, issues, ongoing projects, etc: <el-link type='primary' href="https://groups.google.com/g/ampsphere-users">Go to our community now!</el-link></p>
        <p>This is a project hosted by the <el-link type='primary' href="big-data-biology.org/">Big Data Biology Research Group</el-link>, visit us at this link!</p>
        <hr />

<!--     TODO two columns: names go to the left side, and affiliation goes to the right side.-->

        <h3 id="contact-us-if-you-have-issues-or-suggestions">Contact us if you have issues or suggestions:</h3>
        <el-row>
          <el-col :span="11">
            <p><strong>To direct communication:</strong></p>
            <ul>
              <li><el-link type='primary' href="mailto:celio@big-data-biology.org">Célio Dias Santos Júnior</el-link></li>
              <li><el-link type='primary' href="mailto:hui@big-data-biology.org">Hui Chong</el-link></li>
              <li><el-link type='primary' href="mailto:luis@luis.org">Luis Pedro Coelho</el-link></li>
            </ul>
          </el-col>
          <el-col :span="11" :offset="1">
            <p><strong>Affiliation:</strong></p>
            <p>Institute of Science and Technology for Brain-Inspired Intelligence (<el-link type='primary' href="istbi.fudan.edu.cn/">ISTBI</el-link>). 23rd Floor, East Main Building of Guanghua Tower Fudan University 220 Handan Road, Yangpu District Shanghai(200433), China.</p>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Contact"
}
</script>

<style scoped>

</style>