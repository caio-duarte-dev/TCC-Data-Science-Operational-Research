import time
from src.pipeline.run_solver import run


def main():
    start = time.perf_counter()

    run()

    end = time.perf_counter()

    total = end - start
    minutos = int(total // 60)
    segundos = total % 60

    print("\n==============================")
    print("PIPELINE FINALIZADO")
    print(f"Tempo total: {minutos} min {segundos:.2f} s")
    print("==============================\n")


if __name__ == "__main__":
    main()