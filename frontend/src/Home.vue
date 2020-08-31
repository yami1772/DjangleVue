<template>
  <div class="home">
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入姓名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addStu()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
        <el-table :data="stuList" style="width: 100%" border>
          <el-table-column prop="id" label="编号" min-width="100">
            <template slot-scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="name" label="姓名" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.book_name }} </template>
          </el-table-column>
          <el-table-column prop="StudentNum" label="学号" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
        </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      stuList: [],
    }
  },
  mounted: function() {
      this.showStu()
  },
  methods: {
    // addStu(){
    //   this.$axios.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
    //     .then((res) => {
    //         // console.log(res)
    //         var res = res.data;
    //         if (res.error_num == 0) {
    //           this.showStu()
    //         } else {
    //           this.$message.error('新增书籍失败，请重试')
    //           console.log(res['msg'])
    //         }
    //     })
    // },
    addStu(){
        console.log('no class function found')
    },
    showStu(){
      this.$axios.get('0:9000/stu/show_list')
        .then((res) => {
            var res = res.data;
            // console.log(res)
            if (res.error_num == 0) {
              this.stuList = res['list']
            } else {
              this.$message.error('查询书籍失败')
              console.log(res['msg'])
            }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>

