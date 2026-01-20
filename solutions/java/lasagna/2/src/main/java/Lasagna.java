public class Lasagna {
    int expectedtimeinoven = 40;
    int prepperlayer = 2;
    public int expectedMinutesInOven() {
        return expectedtimeinoven;
    }
    public int remainingMinutesInOven(int x) {
        return expectedtimeinoven - x;
    }
    public int preparationTimeInMinutes(int x) {
        return prepperlayer * x;
    }
    public int totalTimeInMinutes(int x, int y) {
        return (prepperlayer * x) + y;
    }
}