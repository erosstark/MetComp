from manim import *
import numpy as np

class SphericalPendulum(Scene):
    def construct(self):
        # Dados da simulação
        x_data = [...]  # suas coordenadas x
        y_data = [...]  # suas coordenadas y
        z_data = [...]  # suas coordenadas z
        t_data = [...]  # seus tempos

        # Verificar se os dados estão alinhados
        assert len(x_data) == len(y_data) == len(z_data) == len(t_data), "Os dados devem ter o mesmo comprimento"

        pendulum_origin = ORIGIN
        pendulum_mass = Dot(pendulum_origin)
        rod = Line(pendulum_origin, pendulum_mass.get_center())
        self.add(rod, pendulum_mass)

        def update_pendulum(mob, alpha):
            # Encontrar o índice correspondente ao valor de alpha
            idx = min(int(alpha * len(t_data)), len(t_data) - 1)
            x = x_data[idx]
            y = y_data[idx]
            z = z_data[idx]

            # Atualizar a posição do pêndulo
            new_position = np.array([x, y, z])
            pendulum_mass.move_to(new_position)
            rod.put_start_and_end_on(pendulum_origin, pendulum_mass.get_center())

        self.play(UpdateFromAlphaFunc(pendulum_mass, update_pendulum, run_time=10))

if __name__ == "__main__":
    scene = SphericalPendulum()
    scene.render()
