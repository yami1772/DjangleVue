<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js App"/>

        <el-button type="primary" @click="GetData">获取数据</el-button>
        <br>
        <span>姓名：{{name}}</span>
        <br>
        <span>年龄：{{age}}</span>

    </div>
</template>

<script>
    // @ is an alias to /src
    import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'Home',
        components: {
            HelloWorld
        },
        data() {
            return {
                name: '',
                age: ''
            }
        },
        methods: {
            GetData() {
                this.$http.get('/api/user/').then(  //  路径'/api/user/'为django后端对应的url路径
                    res => {
                        if (res.data.length > 0){
                            this.name = res.data[0].name
                            this.age = res.data[0].age
                            this.$message.success('获取用户数据成功')
                        }else {
                            this.$message.warning('后端数据为空')
                        }
                    }
                ).catch(
                    err => {
                        this.$message.error('获取用户数据失败')
                    }
                )
            }
        }
    }
</script>
