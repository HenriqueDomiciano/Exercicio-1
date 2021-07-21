<script>
import {Line} from 'vue3-chart-v2';
export default {
    extends :Line,
    props: {
        label2:{
            type:String
        },
        label:{
            type:String
        },
        chartData : {
            type:Array
        },
        secondData: {
            type:Array
        },
        options:{
            type:Object
        }
    },
    mounted(){
        const dates = this.chartData.map(d=>d.date)
        const totals = this.chartData.map(d=>d.total)
            
        if (this.secondData.length==0){
            this.renderChart({
                labels:dates,
                datasets:[{
                    label : this.label,
                    data : totals,
                    borderColor: 'rgb(75, 192, 192)',
                    fill:false
                },
                ]
            
            }
            ,this.options
        )    
        }
        else{
            const totals2 = this.secondData.map(d=>d.total)
            this.renderChart({
                labels:dates,
                datasets:[{
                    label : this.label,
                    data : totals,
                    borderColor: 'rgb(75, 192, 192)',
                    fill:false
                },
                {
                    label : this.label2,
                    data: totals2,
                    borderColor:'rgb(75, 230, 192)'
                }
                ]
            
            }
            ,this.options
        )    
        }
    }
}
</script>