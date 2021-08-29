<template>
    <div>
        <v-data-table
                :headers="headers"
                :items="desserts"
                :items-per-page="5"
                class="elevation-1"
        >
            <template v-slot:item.actions="{item}">
                <v-btn small color="green" @click="checkReport(item)">查看报告</v-btn>
            </template>
        </v-data-table>

    </div>
</template>

<script>
    export default {
        created() {
            this.getTaskList()
        },
        methods: {
            getTaskList() {
                this.$api.task.getTask().then((result) => {
                    this.desserts = result['data']['msg']['data']
                })
            },
            checkReport(item) {
                window.open(item.report)
            },
        },
        data() {
            return {

                headers: [
                    {
                        text: '任务ID',
                        align: 'start',
                        sortable: false,
                        value: 'id',
                    },
                    {text: '任务描述', value: 'remark'},
                    {text: '创建时间', value: 'create_at', sortable: true},
                    {text: 'Actions', value: 'actions', sortable: false},
                ],
                desserts: [
                    {
                        id: 'Frozen Yogurt',
                        remark: 159,
                    },
                ],
            }
        },
    }
</script>

<style scoped>

</style>