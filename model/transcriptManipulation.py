def stripCallerText(transcription):
	transcript_lines = transcription.split('\n')
	caller_lines = [line.split(": ")[1] for line in transcript_lines if "Operator: " not in line]
	return "\n".join(caller_lines)

def stripOperatorText(transcription):
	transcript_lines = transcription.split('\n')
	operator_lines = [line.split(": ")[1] for line in transcript_lines if "Operator: " in line]
	return "\n".join(operator_lines)