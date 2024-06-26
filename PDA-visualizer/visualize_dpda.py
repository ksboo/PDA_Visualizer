from automata.pda.dpda import DPDA  # Import DPDA instead of NPDA
from automata.base.exceptions import RejectionException
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class PushDownAutomata:
    def create_dpda(
        input_states,
        input_alphabets,
        input_stack_alphabets,
        input_transitions,
        input_initial_state,
        input_initial_stack_symbol,
        input_final_states,
        input_acceptance_mode,
    ):
        dpda = DPDA(
            states=input_states,
            input_symbols=input_alphabets,
            stack_symbols=input_stack_alphabets,
            transitions=input_transitions,
            initial_state=input_initial_state,
            initial_stack_symbol=input_initial_stack_symbol,
            final_states=input_final_states,
            acceptance_mode=input_acceptance_mode,
        )
        return dpda

    def validate_dpda(dpda):  # Rename validate_npda to validate_dpda
        if dpda.validate():
            return False
        else:
            dpda.show_diagram(path="static/dpda/diagram.png")  # Update path
            return True

    def simulate_dpda(input_string, dpda):  # Rename simulate_npda to simulate_dpda
        if input_string == "E":
            input_string = ""

        is_accepted = dpda.accepts_input(input_string)

        if input_string == "":
            input_string = "E"
        plot_path = f"static/dpda/tests/test-{input_string}.png"  # Update path

        if is_accepted:
            if input_string == "E":
                input_string = ""
            dpda.show_diagram(input_str=input_string, path=plot_path, with_stack=True)
            if input_string == "":
                input_string = "E"
            return True, input_string, f"{input_string} is accepted!"
        else:
            return False, input_string, f"{input_string} is not accepted!"
