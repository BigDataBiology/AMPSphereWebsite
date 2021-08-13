<template>
  <div id="Contact">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/contact' }">Contact</el-breadcrumb-item>
        </el-breadcrumb>

        <h1>Contact</h1>
        <p>AMPsphere also is discussed in a forum where users can suggest improvements, issues, ongoing projects, etc: <a href="https://groups.google.com/g/ampsphere-users">Go to our community now!</a></p>
        <p>This is a project hosted by the <a href="big-data-biology.org/">Big Data Biology Research Group</a>, visit us at this link!</p>
        <hr />

<!--     TODO two columns: names go to the left side, and affiliation goes to the right side.-->

        <h3 id="contact-us-if-you-have-issues-or-suggestions">Contact us if you have issues or suggestions:</h3>
        <p>To direct communication:</p>
        <ul>
          <li><a href="mailto:celio@big-data-biology.org">Célio Dias Santos Júnior</a></li>
          <li><a href="mailto:hui@big-data-biology.org">Hui Chong</a></li>
          <li><a href="mailto:luis@luis.org">Luis Pedro Coelho</a></li>
        </ul>
        <p><strong>Affiliation:</strong></p>
        <p>Institute of Science and Technology for Brain-Inspired Intelligence (<a href="istbi.fudan.edu.cn/">ISTBI</a>). 23rd Floor, East Main Building of Guanghua Tower Fudan University 220 Handan Road, Yangpu District Shanghai(200433), China.</p>


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