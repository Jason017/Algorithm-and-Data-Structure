class CyclicRotation {
    public int[] solution(int[] A, int K) {
        int [] rotatedA = new int[A.length];

        for(int i=0; i<A.length; i++) {
            int rotatedIndex = (i + K) % A.length;
            rotatedA[rotatedIndex] = A[i];
        }
        return rotatedA;
    }
}