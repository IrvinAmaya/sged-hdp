const getOptionChart2 = async () => {
    try {
        const response = await fetch("https://sg-estudiantes-discapacitados.onrender.com/get_chart2/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChart2 = async () => {
    const myChart = echarts.init(document.getElementById("chart2"));

    myChart.setOption(await getOptionChart2());

    myChart.resize();
};

window.addEventListener("load", async () => {
    await initChart2();
    setInterval(async () => {
        await initChart2();
    }, 2000);
});